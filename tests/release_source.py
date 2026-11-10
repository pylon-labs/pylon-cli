"""Test the real release-source gate against isolated local Git repositories."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import tomllib


script = Path('.github/scripts/verify-release-source.sh').resolve()
with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    origin = root / 'origin.git'
    checkout = root / 'checkout'
    mock_bin = root / 'bin'
    mock_bin.mkdir()
    mock_gh = mock_bin / 'gh'
    mock_gh.write_text('#!/usr/bin/env bash\nprintf "%s\\n" "${MOCK_ROLE:-maintain}"\n')
    mock_gh.chmod(0o755)
    env = {**os.environ, 'PATH': f'{mock_bin}{os.pathsep}{os.environ["PATH"]}',
           'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REF': 'refs/heads/main',
           'GITHUB_REPOSITORY': 'pylon-labs/pylon-cli', 'GITHUB_ACTOR': 'fixture',
           'GITHUB_TRIGGERING_ACTOR': 'fixture', 'GH_TOKEN': 'FAKE_GITHUB_TOKEN',
           'REQUESTED_TAG': 'v0.1.0', 'GITHUB_OUTPUT': str(root / 'outputs')}

    def git(*args, cwd=None):
        return subprocess.check_output(['git', *args], cwd=cwd or checkout, stderr=subprocess.DEVNULL, text=True).strip()

    subprocess.run(['git', 'init', '--bare', str(origin)], check=True, capture_output=True)
    subprocess.run(['git', 'init', '--initial-branch=main', str(checkout)], check=True, capture_output=True)
    git('config', 'user.name', 'Release Fixture')
    git('config', 'user.email', 'fixture@example.invalid')
    (checkout / 'Cargo.toml').write_text('[package]\nname = "pylon"\nversion = "0.1.0"\n')
    git('add', 'Cargo.toml')
    git('commit', '-m', 'Reviewed source fixture')
    sha = git('rev-parse', 'HEAD')
    git('remote', 'add', 'origin', str(origin))
    git('tag', 'v0.1.0')
    git('tag', 'v0.9.0')
    git('push', '--quiet', 'origin', 'main', '--tags')

    def gate(success, **overrides):
        output = Path(env['GITHUB_OUTPUT'])
        output.unlink(missing_ok=True)
        result = subprocess.run(['bash', str(script)], cwd=checkout, env={**env, **overrides},
                                capture_output=True, text=True, timeout=15)
        assert (result.returncode == 0) == success, result.stdout + result.stderr
        return output.read_text() if output.exists() else ''

    assert f'sha={sha}' in gate(True)
    assert 'publishing=false' in gate(True, GITHUB_EVENT_NAME='pull_request')
    gate(True, MOCK_ROLE='write')
    gate(False, MOCK_ROLE='read')
    gate(False, MOCK_ROLE='triage')
    gate(True, AUTHORIZE_ONLY='true', REQUESTED_VERSION='0.1.1', REQUESTED_TAG='')
    gate(True, AUTHORIZE_ONLY='true')
    gate(False, AUTHORIZE_ONLY='true', REQUESTED_VERSION='0.1.1')
    gate(False, AUTHORIZE_ONLY='true', REQUESTED_TAG='')
    gate(False, AUTHORIZE_ONLY='true', MOCK_ROLE='read')
    gate(False, GITHUB_REF='refs/heads/feature')
    gate(False, REQUESTED_TAG='v0.1.0$(touch rejected)')
    gate(False, REQUESTED_TAG='v0.9.0')
    gate(False, EXPECTED_RELEASE_SHA='0' * 40)
    (checkout / 'later.txt').write_text('A later reviewed commit')
    git('add', 'later.txt')
    git('commit', '-m', 'Main advanced after release selection')
    git('push', '--quiet', 'origin', 'main')
    gate(False)
    assert not (checkout / 'rejected').exists()
    print('Release gate checks passed: writer permissions, protected source, exact version, and stale-source rejection')


prepare_script = Path('.github/scripts/prepare-release.sh').resolve()
bump_script = Path('.github/scripts/bump-version.py').resolve()
mock_release_gh = '''#!/usr/bin/env python3
import json
import os
from pathlib import Path
import subprocess
import sys

args = sys.argv[1:]
origin = os.environ['MOCK_ORIGIN']
scenario = os.environ['MOCK_SCENARIO']
def git(*args):
    return subprocess.check_output(['git', *args], stderr=subprocess.DEVNULL, text=True).strip()
if args[:2] == ['auth', 'setup-git']:
    pass
elif args[:2] == ['pr', 'list']:
    print('[{"number": 1}]' if scenario == 'existing-pr' else '[]')
elif args[:2] == ['pr', 'create']:
    print('Created fixture version bump')
elif args[:2] == ['pr', 'view']:
    if args[args.index('--json') + 1] == 'mergeCommit':
        print(git('--git-dir', origin, 'rev-parse', 'refs/heads/main'))
    else:
        head = git('--git-dir', origin, 'rev-parse', 'refs/heads/release/v0.1.1')
        marker = Path(os.environ['MOCK_POLLED'])
        checks = []
        if marker.exists() or scenario != 'pending':
            checks = [{'name': name, 'status': 'COMPLETED',
                       'conclusion': 'FAILURE' if scenario == 'failed-check' else 'SUCCESS'}
                      for name in ('release-ready', 'verify-distribution')]
        marker.touch()
        print(json.dumps({'number': 1, 'state': 'OPEN', 'headRefOid': '0' * 40 if scenario == 'changed-head' else head,
                          'statusCheckRollup': checks}))
elif args[:2] == ['pr', 'merge']:
    head = git('--git-dir', origin, 'rev-parse', 'refs/heads/release/v0.1.1')
    assert args[args.index('--match-head-commit') + 1] == head
    git('push', '--quiet', 'origin', head + ':refs/heads/main')
    git('push', '--quiet', 'origin', '--delete', 'release/v0.1.1')
    if scenario == 'main-advanced':
        Path('later.txt').write_text('Another change after the version bump')
        git('add', 'later.txt')
        git('commit', '-m', 'Another merge')
        git('push', '--quiet', 'origin', 'HEAD:main')
elif args[0] == 'api' and args[1].endswith('/git/refs'):
    ref = next(value[4:] for value in args if value.startswith('ref='))
    sha = next(value[4:] for value in args if value.startswith('sha='))
    git('--git-dir', origin, 'update-ref', ref, sha, '0' * 40)
else:
    raise AssertionError(args)
'''

for scenario in ('success', 'pending', 'failed-check', 'changed-head', 'main-advanced',
                 'existing-tag', 'existing-pr', 'orphan-branch', 'stale-branch', 'invalid-version',
                 'downgrade', 'lock-mismatch', 'resume-bump'):
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        origin, checkout, mock_bin = root / 'origin.git', root / 'checkout', root / 'bin'
        mock_bin.mkdir()
        (mock_bin / 'gh').write_text(mock_release_gh)
        (mock_bin / 'gh').chmod(0o755)
        (mock_bin / 'sleep').write_text('#!/usr/bin/env bash\nexit 0\n')
        (mock_bin / 'sleep').chmod(0o755)
        subprocess.run(['git', 'init', '--bare', str(origin)], check=True, capture_output=True)
        subprocess.run(['git', 'init', '--initial-branch=main', str(checkout)], check=True, capture_output=True)
        git('config', 'user.name', 'Release Fixture')
        git('config', 'user.email', 'fixture@example.invalid')
        scripts = checkout / '.github/scripts'
        scripts.mkdir(parents=True)
        shutil.copy(bump_script, scripts / bump_script.name)
        current = '0.1.1' if scenario == 'resume-bump' else '0.1.0'
        (checkout / 'Cargo.toml').write_text(f'[package]\nname = "pylon"\nversion = "{current}"\n')
        locked = '0.0.9' if scenario == 'lock-mismatch' else current
        (checkout / 'Cargo.lock').write_text(
            f'version = 4\n\n[[package]]\nname = "pylon"\nversion = "{locked}"\n\n'
            '[[package]]\nname = "dependency"\nversion = "5.0.0"\nsource = "registry+fixture"\n')
        git('add', '.')
        git('commit', '-m', 'Reviewed release preparation fixture')
        initial_sha = git('rev-parse', 'HEAD')
        git('remote', 'add', 'origin', str(origin))
        git('push', '--quiet', 'origin', 'main')
        if scenario == 'existing-tag':
            git('tag', 'v0.1.1')
            git('push', '--quiet', 'origin', 'v0.1.1')
        if scenario in ('existing-pr', 'orphan-branch', 'stale-branch'):
            git('checkout', '-b', 'release/v0.1.1')
            subprocess.run(['python3', str(bump_script)], cwd=checkout,
                           env={**os.environ, 'VERSION': '0.1.1'}, check=True, capture_output=True)
            git('add', 'Cargo.toml', 'Cargo.lock')
            git('commit', '-m', 'Existing version bump')
            if scenario == 'stale-branch':
                (checkout / 'unexpected.txt').write_text('Unrelated source change')
                git('add', 'unexpected.txt')
                git('commit', '-m', 'Unexpected branch change')
            git('push', '--quiet', 'origin', 'HEAD')
            git('checkout', 'main')
            git('branch', '-D', 'release/v0.1.1')
        version = {'invalid-version': '0.1.1$(touch rejected)', 'downgrade': '0.0.1'}.get(scenario, '0.1.1')
        env = {**os.environ, 'PATH': f'{mock_bin}{os.pathsep}{os.environ["PATH"]}',
               'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REF': 'refs/heads/main',
               'GITHUB_REPOSITORY': 'pylon-labs/pylon-cli', 'VERSION': version,
               'GITHUB_OUTPUT': str(root / 'outputs'), 'MOCK_ORIGIN': str(origin),
               'MOCK_SCENARIO': scenario, 'MOCK_POLLED': str(root / 'polled')}
        result = subprocess.run(['bash', str(prepare_script)], cwd=checkout, env=env,
                                capture_output=True, text=True, timeout=15)
        expected_success = scenario in ('success', 'pending', 'existing-pr', 'orphan-branch', 'resume-bump')
        assert (result.returncode == 0) == expected_success, (scenario, result.stdout, result.stderr)
        refs = git('--git-dir', str(origin), 'show-ref')
        if expected_success:
            main_sha = git('--git-dir', str(origin), 'rev-parse', 'refs/heads/main')
            assert f'{main_sha} refs/tags/v0.1.1' in refs
            assert (root / 'outputs').read_text() == 'tag=v0.1.1\n'
            assert tomllib.loads((checkout / 'Cargo.toml').read_text())['package']['version'] == '0.1.1'
            lock = tomllib.loads((checkout / 'Cargo.lock').read_text())
            assert [package['version'] for package in lock['package']] == ['0.1.1', '5.0.0']
        else:
            assert not (root / 'outputs').exists()
            if scenario != 'existing-tag':
                assert 'refs/tags/v0.1.1' not in refs
            if scenario not in ('main-advanced',):
                assert git('--git-dir', str(origin), 'rev-parse', 'refs/heads/main') == initial_sha
        assert not (checkout / 'rejected').exists()
print('Release preparation checks passed: checked merge, pending checks, retries, immutable tags, and failure rejection')

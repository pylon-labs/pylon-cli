"""Test the real release-source gate against isolated local Git repositories."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile


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

    def git(*args, cwd=checkout):
        return subprocess.check_output(['git', *args], cwd=cwd, stderr=subprocess.DEVNULL, text=True).strip()

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
    gate(False, MOCK_ROLE='write')
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
    print('Release gate checks passed: maintainer, protected source, exact version, and stale-source rejection')

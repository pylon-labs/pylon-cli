"""Validate publication checks without creating or publishing a release."""

import hashlib
from pathlib import Path
import subprocess
import tempfile


script = Path('.github/scripts/verify-artifacts.sh').resolve()
archives = [
    'pylon-aarch64-apple-darwin.tar.gz', 'pylon-x86_64-apple-darwin.tar.gz',
    'pylon-aarch64-unknown-linux-musl.tar.gz', 'pylon-x86_64-unknown-linux-musl.tar.gz',
    'pylon-x86_64-pc-windows-msvc.zip', 'source.tar.gz',
]

with tempfile.TemporaryDirectory() as directory:
    root = Path(directory)
    for name in [*archives, 'pylon-installer.sh', 'pylon-installer.ps1', 'dist-manifest.json']:
        (root / name).write_text(f'Fixture bytes for {name}')
    (root / 'sha256.sum').write_text(''.join(
        f'{hashlib.sha256((root / name).read_bytes()).hexdigest()} *{name}\n' for name in archives
    ))

    def check(success):
        result = subprocess.run(['bash', str(script), str(root)], capture_output=True, text=True, timeout=10)
        assert (result.returncode == 0) == success, result.stdout + result.stderr

    check(True)
    nested = root / 'target' / 'distrib'
    nested.mkdir(parents=True)
    check(False)
    nested.rmdir()
    nested.parent.rmdir()
    original = (root / archives[0]).read_bytes()
    (root / archives[0]).write_text('Tampered bytes')
    check(False)
    (root / archives[0]).write_bytes(original)
    installer = (root / 'pylon-installer.sh').read_bytes()
    (root / 'pylon-installer.sh').unlink()
    check(False)
    (root / 'pylon-installer.sh').write_bytes(installer)
    check(True)
    print('Distribution checks passed: complete flat bundle required; nested, missing and altered assets rejected')

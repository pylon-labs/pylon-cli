"""Update only the CLI package version, preserving the dependency lockfile."""

import os
from pathlib import Path
import re
import tomllib


def version_key(version):
    match = re.fullmatch(r'(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-([0-9A-Za-z.-]+))?', version)
    if not match:
        raise ValueError('Expected a semantic version without a v prefix')
    prerelease = match[4]
    identifiers = prerelease.split('.') if prerelease else []
    if any(not value or (value.isdigit() and len(value) > 1 and value.startswith('0')) for value in identifiers):
        raise ValueError('Invalid semantic version prerelease')
    return (
        *(int(match[index]) for index in (1, 2, 3)),
        prerelease is None,
        tuple((not value.isdigit(), int(value) if value.isdigit() else value) for value in identifiers),
    )


def replace_version(block, version):
    result, count = re.subn(r'(?m)^version = "[^"]+"$', f'version = "{version}"', block)
    if count != 1:
        raise ValueError('Expected exactly one package version')
    return result


def bump(version):
    requested = version_key(version)
    manifest_path, lock_path = Path('Cargo.toml'), Path('Cargo.lock')
    manifest, lock = manifest_path.read_text(), lock_path.read_text()
    package = tomllib.loads(manifest)['package']
    if requested < version_key(package['version']):
        raise ValueError('Cannot release a version older than the current package version')

    manifest_blocks = re.split(r'(?m)(?=^\[)', manifest)
    package_blocks = [index for index, block in enumerate(manifest_blocks) if block.startswith('[package]\n')]
    if len(package_blocks) != 1:
        raise ValueError('Expected one root package')
    index = package_blocks[0]
    manifest_blocks[index] = replace_version(manifest_blocks[index], version)

    lock_blocks = re.split(r'(?m)(?=^\[\[package\]\]$)', lock)
    matches = []
    for index, block in enumerate(lock_blocks):
        if not block.startswith('[[package]]\n'):
            continue
        locked = tomllib.loads(block)['package'][0]
        if locked['name'] == package['name'] and 'source' not in locked:
            if locked['version'] != package['version']:
                raise ValueError('Cargo.toml and Cargo.lock versions disagree')
            matches.append(index)
    if len(matches) != 1:
        raise ValueError('Expected one local CLI package in Cargo.lock')
    index = matches[0]
    lock_blocks[index] = replace_version(lock_blocks[index], version)

    manifest_path.write_text(''.join(manifest_blocks))
    lock_path.write_text(''.join(lock_blocks))


if __name__ == '__main__':
    bump(os.environ['VERSION'])

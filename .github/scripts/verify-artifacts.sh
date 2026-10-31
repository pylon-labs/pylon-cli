#!/usr/bin/env bash
set -euo pipefail
cd "$1"

if [[ -n "$(find . -mindepth 1 -maxdepth 1 -type d -print -quit)" ]]; then
	echo 'Release assets must be flat files, not nested artifact directories.' >&2
	exit 1
fi
for asset in \
	pylon-aarch64-apple-darwin.tar.gz \
	pylon-x86_64-apple-darwin.tar.gz \
	pylon-aarch64-unknown-linux-musl.tar.gz \
	pylon-x86_64-unknown-linux-musl.tar.gz \
	pylon-x86_64-pc-windows-msvc.zip \
	pylon-installer.sh pylon-installer.ps1 source.tar.gz dist-manifest.json sha256.sum; do
	if [[ ! -f "$asset" || -L "$asset" ]]; then
		echo "Missing or nonregular release asset: $asset" >&2
		exit 1
	fi
done

# Cargo-dist records archive/source checksums. Release attestations also cover installers.
if command -v sha256sum >/dev/null; then
	sha256sum -c sha256.sum
else
	shasum -a 256 -c sha256.sum
fi

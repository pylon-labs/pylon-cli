#!/usr/bin/env bash
set -euo pipefail

case "$(uname -s)-$(uname -m)" in
	Darwin-arm64) dist_host=aarch64-apple-darwin; dist_sha=decb01c64c12501931c3cac3111b368a7f48adf8d9e65455c08e5757b9a1fd6f ;;
	Darwin-x86_64) dist_host=x86_64-apple-darwin; dist_sha=fd4d8f9f07802359cbcdc52bac3abd7d5201c4b73a7cbcdd6faca2232a389f0c ;;
	Linux-aarch64) dist_host=aarch64-unknown-linux-gnu; dist_sha=382cc29ff91ef12a5bf78ad8ee1804661d24e2fbe64b1bdedd6078723b677ae5 ;;
	Linux-x86_64) dist_host=x86_64-unknown-linux-gnu; dist_sha=cd355dab0b4c02fb59038fef87655550021d07f45f1d82f947a34ef98560abb8 ;;
	MINGW*-x86_64|MSYS*-x86_64) dist_host=x86_64-pc-windows-msvc; dist_sha=a14e17557b269b101405e0cc6b647581d56313c954a51c7fddd423bba21e17b2 ;;
	*) echo 'Unsupported cargo-dist host' >&2; exit 1 ;;
esac

dist_suffix=tar.xz
dist_binary=dist
if [[ "$dist_host" == *windows* ]]; then
	dist_suffix=zip
	dist_binary=dist.exe
fi
dist_work=$(mktemp -d)
trap 'rm -rf "$dist_work"' EXIT
dist_archive="cargo-dist-$dist_host.$dist_suffix"
curl --proto '=https' --tlsv1.2 -fsSL \
	"https://github.com/axodotdev/cargo-dist/releases/download/v0.31.0/$dist_archive" \
	-o "$dist_work/$dist_archive"
if command -v sha256sum >/dev/null; then
	dist_actual=$(sha256sum "$dist_work/$dist_archive")
else
	dist_actual=$(shasum -a 256 "$dist_work/$dist_archive")
fi
if [[ "${dist_actual%% *}" != "$dist_sha" ]]; then
	echo 'cargo-dist checksum mismatch' >&2
	exit 1
fi
if [[ "$dist_suffix" == zip ]]; then
	unzip -q "$dist_work/$dist_archive" -d "$dist_work"
else
	tar -xJf "$dist_work/$dist_archive" -C "$dist_work"
fi
mkdir -p "$RUNNER_TEMP/pylon-dist/bin"
cp "$dist_work/cargo-dist-$dist_host/$dist_binary" "$RUNNER_TEMP/pylon-dist/bin/$dist_binary"
chmod +x "$RUNNER_TEMP/pylon-dist/bin/$dist_binary"
echo "$RUNNER_TEMP/pylon-dist/bin" >> "$GITHUB_PATH"

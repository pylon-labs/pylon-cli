#!/usr/bin/env bash
set -euo pipefail

if [[ "$GITHUB_EVENT_NAME" != workflow_dispatch ]]; then
	echo "sha=$(git rev-parse HEAD)" >> "$GITHUB_OUTPUT"
	echo 'tag=' >> "$GITHUB_OUTPUT"
	echo 'publishing=false' >> "$GITHUB_OUTPUT"
	exit 0
fi
if [[ "$GITHUB_REF" != refs/heads/main ]]; then
	echo 'Start releases from the protected main workflow.' >&2
	exit 1
fi
if [[ ! "$REQUESTED_TAG" =~ ^v[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?$ ]]; then
	echo 'A release tag must be vMAJOR.MINOR.PATCH, optionally with a prerelease suffix.' >&2
	exit 1
fi
release_actor="${GITHUB_TRIGGERING_ACTOR:-$GITHUB_ACTOR}"
release_role=$(gh api "repos/$GITHUB_REPOSITORY/collaborators/$release_actor/permission" --jq .role_name)
if [[ "$release_role" != admin && "$release_role" != maintain ]]; then
	echo 'A repository maintainer or administrator must start the release.' >&2
	exit 1
fi
git fetch --quiet --no-tags origin '+refs/heads/main:refs/remotes/origin/main' \
	"refs/tags/$REQUESTED_TAG:refs/tags/$REQUESTED_TAG"
release_sha=$(git rev-parse --verify "refs/tags/$REQUESTED_TAG^{commit}")
main_sha=$(git rev-parse --verify refs/remotes/origin/main)
if [[ "$release_sha" != "$main_sha" || "$(git rev-parse HEAD)" != "$main_sha" ]]; then
	echo 'The version tag, selected source, and current reviewed main must identify the same commit.' >&2
	exit 1
fi
release_version=$(sed -n 's/^version = "\([^"]*\)"$/\1/p' Cargo.toml | head -1)
if [[ "$REQUESTED_TAG" != "v$release_version" ]]; then
	echo 'The tag must match the Cargo package version.' >&2
	exit 1
fi
if [[ -n "${EXPECTED_RELEASE_SHA:-}" && "$release_sha" != "$EXPECTED_RELEASE_SHA" ]]; then
	echo 'Release source changed after validation.' >&2
	exit 1
fi
echo "sha=$release_sha" >> "$GITHUB_OUTPUT"
echo "tag=$REQUESTED_TAG" >> "$GITHUB_OUTPUT"
echo 'publishing=true' >> "$GITHUB_OUTPUT"

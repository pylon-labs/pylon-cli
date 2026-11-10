#!/usr/bin/env bash
set -euo pipefail

if [[ "$GITHUB_EVENT_NAME" != workflow_dispatch || "$GITHUB_REF" != refs/heads/main ]]; then
	echo 'Prepare releases only from the protected main workflow.' >&2
	exit 1
fi

gh auth setup-git --hostname github.com
git fetch --quiet --tags origin '+refs/heads/main:refs/remotes/origin/main'
git checkout --detach origin/main
python3 .github/scripts/bump-version.py
tag="v$VERSION"
branch="release/$tag"
if git show-ref --verify --quiet "refs/tags/$tag"; then
	echo "The immutable tag $tag already exists; inspect the previous release before continuing." >&2
	exit 1
fi

if ! git diff --quiet -- Cargo.toml Cargo.lock; then
	git config user.name 'github-actions[bot]'
	git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
	git checkout -b "$branch"
	git add Cargo.toml Cargo.lock
	git commit -m "Release $tag"
	prs=$(gh pr list --repo "$GITHUB_REPOSITORY" --base main --head "$branch" --state open --json number)
	remote_branch=$(git ls-remote --heads origin "refs/heads/$branch")
	if [[ -n "$remote_branch" ]]; then
		git fetch --quiet origin "refs/heads/$branch"
		if ! git diff --quiet HEAD FETCH_HEAD; then
			echo "Existing $branch differs from the requested version bump on current main; inspect its pull request." >&2
			exit 1
		fi
		git checkout --detach FETCH_HEAD
	else
		git push origin "HEAD:refs/heads/$branch"
	fi
	if [[ "$(jq 'length' <<< "$prs")" == 0 ]]; then
		gh pr create --repo "$GITHUB_REPOSITORY" --base main --head "$branch" \
			--title "Release $tag" --body 'Bump the CLI package version. The release workflow merges this after required checks pass, then tags and publishes the checked source.'
	fi
	release_head=$(git rev-parse HEAD)
	deadline=$((SECONDS + 2700))
	while (( SECONDS < deadline )); do
		pr=$(gh pr view "$branch" --repo "$GITHUB_REPOSITORY" --json number,state,headRefOid,statusCheckRollup)
		if [[ "$(jq -r .state <<< "$pr")" != OPEN || "$(jq -r .headRefOid <<< "$pr")" != "$release_head" ]]; then
			echo 'The version bump pull request was changed or closed during the release.' >&2
			exit 1
		fi
		if jq -e 'any(.statusCheckRollup[]; (.name == "release-ready" or .name == "verify-distribution") and .status == "COMPLETED" and .conclusion != "SUCCESS")' <<< "$pr" >/dev/null; then
			echo 'A required version bump check failed; inspect the pull request.' >&2
			exit 1
		fi
		if jq -e '[.statusCheckRollup[] | select((.name == "release-ready" or .name == "verify-distribution") and .status == "COMPLETED" and .conclusion == "SUCCESS") | .name] | unique | length == 2' <<< "$pr" >/dev/null; then
			break
		fi
		sleep 20
	done
	if (( SECONDS >= deadline )); then
		echo 'Timed out waiting for version bump checks; the pull request remains open.' >&2
		exit 1
	fi
	pr_number=$(jq -r .number <<< "$pr")
	gh pr merge "$pr_number" --repo "$GITHUB_REPOSITORY" --rebase --delete-branch --match-head-commit "$release_head"
	merged_sha=$(gh pr view "$pr_number" --repo "$GITHUB_REPOSITORY" --json mergeCommit --jq .mergeCommit.oid)
	git fetch --quiet origin '+refs/heads/main:refs/remotes/origin/main'
	git checkout --detach origin/main
	if [[ "$(git rev-parse HEAD)" != "$merged_sha" ]] || ! git diff --quiet "$release_head" HEAD; then
		echo 'Main changed during the version bump; inspect the source before retrying.' >&2
		exit 1
	fi
fi

# Creating the ref fails if another actor created it; never move an existing tag.
gh api "repos/$GITHUB_REPOSITORY/git/refs" -f "ref=refs/tags/$tag" -f "sha=$(git rev-parse HEAD)"
echo "tag=$tag" >> "$GITHUB_OUTPUT"

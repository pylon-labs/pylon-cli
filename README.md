# Pylon CLI

Command-line access to the [Pylon REST API](https://docs.usepylon.com/pylon-docs/developer).

## Install

Install on macOS or Linux:

```sh
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/pylon-labs/pylon-cli/releases/latest/download/pylon-installer.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://github.com/pylon-labs/pylon-cli/releases/latest/download/pylon-installer.ps1 | iex"
```

You can also download binaries from [GitHub Releases](https://github.com/pylon-labs/pylon-cli/releases), or build from source with `cargo build --release --locked`.

## Authenticate

Create an API token in Pylon's API token settings. Run `pylon auth login --with-token` to save it with hidden terminal input, or provide it through the `PYLON_TOKEN` process environment variable. Requests use the token owner's Pylon permissions. Use `--base-url https://api.eu.usepylon.com` for an EU organization.

macOS and Windows use their native credential stores when available. Linux static builds use a plaintext file in the user's config directory, restricted to the owner on Unix. If no private config directory is available, use `PYLON_TOKEN`; the CLI does not read credentials from a shared temporary directory. Repository `.env` files are not loaded automatically.

## Use

```sh
pylon --help
pylon me get
pylon issues search --help
pylon issues search --json '{"filter":{"field":"state","operator":"equals","value":"waiting_on_customer"}}'
pylon issues bulk-update --help
```

Commands use kebab-case, including `bulk-update` and `create-ai-response`. Each command supports `--schema` for machine-readable input documentation, `--dry-run` to inspect its request without sending it, and `--query` for JMESPath output projection. `pylon generate-skills` generates instructions for coding agents.

JSON request bodies and object/array flags preserve strings literally, including text starting with `@`. Local file uploads require explicit file/upload parameters; customer text cannot select a local file merely by appearing in JSON. Table output strips terminal control characters, while JSON output preserves the original values with JSON escaping.

### Pagination and output

JSON is the default in both terminals and pipes, preserving the full API response. Use `--format table` (or `--human`) for a human-readable table. `PYLON_OUTPUT` can override the default; an explicit `--format` takes precedence.

Commands fetch one page unless `--page-all` is set. `--page-all` follows pagination until no next cursor remains. Use `--page-limit N` for an explicit positive page cap; the CLI warns on stderr if it reaches that cap while more results remain. A nonempty `pagination.cursor` means more results remain. Failed requests return a nonzero exit code, even if earlier pages were already printed.

```sh
pylon issues search --json '{"filter":{"field":"state","operator":"equals","value":"waiting_on_customer"}}' \
  --page-all --page-delay 500 --format jsonl > pages.jsonl
```

The API response envelope is preserved: `data`, `pagination`, and `request_id`. Without `--query`, the export above contains one page per line. For a single page, project rows with `--query 'data[]'`. With `--page-all`, queries run over the collected pages, so use `--query '[].data[]'`. A query can hide the cursor; export the envelopes first when you need to verify completeness. `--page-delay` is in milliseconds; rate limits are shared across all callers in the organization.

REST exposes fewer search options than the Pylon MCP server. CLI commands reflect the REST API's options; consult `--help` and `--schema` for supported fields.

## Development and releases

The Pylon monorepo syncs the embedded API spec and command reference through `sync/latest` pull requests. This repository maintains the runtime, tests, README, distribution config, and `.github/` workflows; the sync preserves those files. The sync app has no workflow-write permission.

Run `cargo build --locked`, `cargo test --locked --lib`, `python3 tests/smoke.py`, and `python3 tests/security.py` to check a generated CLI. Integration checks use a local mock API and fake tokens.

To release, open **Actions → Release → Run workflow**, select `main`, and supply the version without a `v` prefix (for example, `0.1.2`). A repository writer, maintainer, or administrator can start the workflow. It opens a version-bump pull request, waits for `release-ready` and `verify-distribution`, merges the checked commit, creates its version tag, and publishes. Tag pushes and ordinary pull request merges do not publish automatically.

One-time setup: install a release GitHub App on this repository with Contents and Pull requests write access, and Checks and Commit statuses read access. Set the repository variable `RELEASE_APP_ID` and secret `RELEASE_APP_PRIVATE_KEY`. Add that app as an always-allowed bypass actor only in the **Restrict release tag creation** ruleset. Do not add it to **Protect release tag history** or allow it to bypass main branch protection. The app token makes the version-bump pull request trigger its checks without a manual workflow approval. Keep the sync app separate from the release app.

Until the app is configured, the existing manual path remains available: merge a checked version-bump pull request, have a maintainer create its tag on current `main`, and dispatch Release with only the `tag` input. That input also supports recovery after a version-input run created its tag but failed before publishing; first inspect the failure and any existing draft or release. The workflow never moves a tag or overwrites a release.

The release workflow verifies the dispatcher's write permissions and requires the tag, checked-out source, Cargo version, and current reviewed `main` to match. It reruns the same Linux/macOS/Windows tests and dependency audit for that exact source, builds every platform, and attests the artifacts. Before publication it revalidates the source, creates a draft, uploads every asset, and publishes the complete immutable GitHub Release. No second person is required to click the release button or approve a PR; changes to `main` still require a PR and passing checks. Existing version tags cannot be rewritten or deleted. A failed run can leave a version-bump pull request; a new dispatch reuses it only when its tree still matches the requested bump on current `main`. If a run already created its tag, inspect the failure instead of dispatching that version again. Another merge to `main` during publication stops the release.

Branch protection requires both `release-ready` and `verify-distribution`. The distribution check assembles the same downloads used for publication, requires a complete flat bundle, and verifies archive checksums. Publication repeats that validation before creating a draft.

The dependency audit uses pinned `cargo-audit` and fails on vulnerabilities or warnings, without ignored advisories. A weekly scheduled run checks for newly reported advisories. This repository owns the reviewed dependency lockfile, which spec synchronization preserves. Update dependency declarations and the lockfile together when upgrading.

Homebrew and npm are not configured. macOS builds do not use an Apple signing certificate; release archives and installers have GitHub provenance attestations. The cargo-dist executable used by CI is checked against a committed SHA-256 before execution.

## Attribution

The generated Rust runtime is built on [Fern's CLI generator](https://github.com/fern-api/fern), Copyright Fern, under the [Apache License 2.0](LICENSE-APACHE). Pylon-authored documentation and setup files use the repository's [MIT license](LICENSE).

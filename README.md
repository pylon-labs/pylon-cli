# Pylon CLI

Command-line access to the [Pylon REST API](https://docs.usepylon.com/pylon-docs/developer).

## Install

Once the first release is published, install on macOS or Linux:

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

**`--page-all` fetches at most 10 pages by default, and stops silently at that limit.** It does not guarantee a complete result. Set `--page-limit` explicitly for large exports, and check the final page's `pagination.cursor` before treating an export or count as complete. A nonempty cursor means more results remain.

```sh
pylon issues search --json '{"filter":{"field":"state","operator":"equals","value":"waiting_on_customer"}}' \
  --page-all --page-limit 1000 --page-delay 500 --format jsonl > pages.jsonl
```

The API response envelope is preserved: `data`, `pagination`, and `request_id`. Without `--query`, the export above contains one page per line. For a single page, project rows with `--query 'data[]'`. With `--page-all`, queries run over the collected pages, so use `--query '[].data[]'`. A query can hide the cursor; export the envelopes first when you need to verify completeness. `--page-delay` is in milliseconds; rate limits are shared across all callers in the organization.

REST exposes fewer search options than the Pylon MCP server. CLI commands reflect the REST API's options; consult `--help` and `--schema` for supported fields.

## Development and releases

The Pylon monorepo owns generation config, distribution config, tests, and this README under `fern/`. Its SDK sync workflow opens `sync/latest` PRs here. Edit generator-owned files in the monorepo so changes survive the next sync. This repository owns its `.github/` workflows, which the generation script backs up and restores. Workflow changes need a maintainer's GitHub credentials; the sync app has no workflow-write permission.

Run `cargo build --locked`, `cargo test --locked --lib`, `python3 tests/smoke.py`, and `python3 tests/security.py` to check a generated CLI. Integration checks use a local mock API and fake tokens.

To release, first merge a reviewed version bump with passing checks. A maintainer or administrator creates the matching tag on current `main` (for example, `v0.1.0`), then opens **Actions → Release → Run workflow**, selects `main`, and supplies that tag. Tag pushes and PR merges do not publish automatically.

The release workflow verifies the maintainer's permissions and requires the tag, checked-out source, Cargo version, and current reviewed `main` to match. It reruns the same Linux/macOS/Windows tests and dependency audit for that exact source, builds every platform, and attests the artifacts. Before publication it revalidates the source, creates a draft, uploads every asset, and publishes the complete immutable GitHub Release. No second person is required to click the release button; changes to `main` still require another review. Existing version tags cannot be rewritten or deleted.

Branch protection requires both `release-ready` and `verify-distribution`. The distribution check assembles the same downloads used for publication, requires a complete flat bundle, and verifies archive checksums. Publication repeats that validation before creating a draft.

The dependency audit uses pinned `cargo-audit` and fails on vulnerabilities or warnings, without ignored advisories. A weekly scheduled run checks for newly reported advisories. The monorepo owns the reviewed dependency lockfile so regeneration cannot restore vulnerable versions. Update dependency customizations and that lockfile together when upgrading.

Homebrew and npm are not configured. macOS builds do not use an Apple signing certificate; release archives and installers have GitHub provenance attestations. The cargo-dist executable used by CI is checked against a committed SHA-256 before execution.

## Attribution

The generated Rust runtime is built on [Fern's CLI generator](https://github.com/fern-api/fern), Copyright Fern, under the [Apache License 2.0](LICENSE-APACHE). Pylon-authored documentation and setup files use the repository's [MIT license](LICENSE).

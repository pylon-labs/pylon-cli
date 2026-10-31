# Pylon CLI

A command-line interface for the [Pylon](https://usepylon.com) REST API.

> **Status:** not yet released. Install instructions will be added with the first release.

The CLI is generated from Pylon's [OpenAPI spec](https://docs.usepylon.com/pylon-docs/developer/api/api-reference) with [Fern](https://buildwithfern.com), alongside the official SDKs:

- TypeScript: [pylon-labs/pylon-typescript](https://github.com/pylon-labs/pylon-typescript)
- Python: [pylon-labs/pylon-python](https://github.com/pylon-labs/pylon-python)
- Go: [pylon-labs/pylon-go](https://github.com/pylon-labs/pylon-go)

## Authentication

The CLI authenticates with a Pylon API token, read from the `PYLON_TOKEN` environment variable or stored with `pylon auth login`. Requests run with the permissions of the user the token belongs to.

## License

[MIT](LICENSE)

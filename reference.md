# Pylon API. CLI Reference

Full command reference for `pylon`.

## Commands

- [`pylon accounts`](#pylon-accounts)
- [`pylon accounts activities`](#pylon-accounts-activities)
- [`pylon accounts email-activities`](#pylon-accounts-email-activities)
- [`pylon accounts highlights`](#pylon-accounts-highlights)
- [`pylon accounts notebook-blocks notes`](#pylon-accounts-notebook-blocks-notes)
- [`pylon accounts relationships`](#pylon-accounts-relationships)
- [`pylon activity-types`](#pylon-activity-types)
- [`pylon article-feedback`](#pylon-article-feedback)
- [`pylon attachments`](#pylon-attachments)
- [`pylon audit-logs`](#pylon-audit-logs)
- [`pylon call-recordings`](#pylon-call-recordings)
- [`pylon contacts`](#pylon-contacts)
- [`pylon custom-fields`](#pylon-custom-fields)
- [`pylon custom-fields select-options`](#pylon-custom-fields-select-options)
- [`pylon custom-objects`](#pylon-custom-objects)
- [`pylon email-suppressions`](#pylon-email-suppressions)
- [`pylon feature-requests`](#pylon-feature-requests)
- [`pylon issue-groups`](#pylon-issue-groups)
- [`pylon issue-groups children`](#pylon-issue-groups-children)
- [`pylon issue-statuses`](#pylon-issue-statuses)
- [`pylon issues`](#pylon-issues)
- [`pylon issues followers`](#pylon-issues-followers)
- [`pylon issues messages`](#pylon-issues-messages)
- [`pylon issues survey-responses`](#pylon-issues-survey-responses)
- [`pylon issues threads`](#pylon-issues-threads)
- [`pylon issues voice-calls`](#pylon-issues-voice-calls)
- [`pylon knowledge-bases`](#pylon-knowledge-bases)
- [`pylon knowledge-bases articles`](#pylon-knowledge-bases-articles)
- [`pylon knowledge-bases collections`](#pylon-knowledge-bases-collections)
- [`pylon knowledge-bases route-redirects`](#pylon-knowledge-bases-route-redirects)
- [`pylon knowledge-bases themes`](#pylon-knowledge-bases-themes)
- [`pylon macro-groups`](#pylon-macro-groups)
- [`pylon macros`](#pylon-macros)
- [`pylon me`](#pylon-me)
- [`pylon milestones`](#pylon-milestones)
- [`pylon projects`](#pylon-projects)
- [`pylon surveys`](#pylon-surveys)
- [`pylon surveys responses`](#pylon-surveys-responses)
- [`pylon tags`](#pylon-tags)
- [`pylon task-statuses`](#pylon-task-statuses)
- [`pylon tasks`](#pylon-tasks)
- [`pylon tasks comments`](#pylon-tasks-comments)
- [`pylon teams`](#pylon-teams)
- [`pylon ticket-forms`](#pylon-ticket-forms)
- [`pylon training-data`](#pylon-training-data)
- [`pylon training-data documents`](#pylon-training-data-documents)
- [`pylon user-roles`](#pylon-user-roles)
- [`pylon user-statuses`](#pylon-user-statuses)
- [`pylon users`](#pylon-users)

---

### `pylon accounts`

#### `pylon accounts bulk-update`

Updates multiple accounts in a single request. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /accounts`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-ids` | `string[]` | Yes | The account IDs to update. The number of accounts to update must be between 1 and 100. |
| `--account-type` | `customer \| partner` | No | The type of the account. Can only be changed to "customer" or "partner". |
| `--custom-fields` | `object[]` | No | An array of custom fields to be updated on the accounts. |
| `--is-disabled` | `boolean` | No | Whether the accounts are disabled. |
| `--owner-id` | `string` | No | The ID of the new owner. If empty string is passed in, the owner will be removed. |
| `--tags` | `string[]` | No | An array of tags to be updated on the accounts. |
| `--tags-apply-mode` | `append_only \| remove_only \| replace` | No | The mode for applying tags. Valid values: "append_only", "remove_only", "replace". Defaults to "replace". |

#### `pylon accounts create`

Creates a new account with the specified name and optional metadata.

**Rate limit:** 300 requests per minute

`POST /accounts`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-type` | `customer \| internal \| community \| partner` | No | The type of the account. Must be one of "customer", "internal", "community", or "partner". Defaults to "customer" if not specified. |
| `--channels` | `object[]` | No | An array of channels to be linked to this account. |
| `--custom-fields` | `object[]` | No | An array of custom fields to be used on this account. |
| `--domain` | `string` | No | Deprecated. Please use Domains and PrimaryDomain instead. |
| `--domains` | `string[]` | No | The domains of the account, without any leading scheme, for example stripe.com. Must specify one domain as primary. |
| `--external-ids` | `object[]` | No | An array of external IDs to be used on this account. If provided, the account's external IDs will be updated to the given external IDs. |
| `--logo-url` | `string` | No | The logo URL of the account. Must be a square .png, .jpg or .jpeg. |
| `--name` | `string` | Yes | The name of the account. |
| `--owner-id` | `string` | No | The ID of the owner of the account. |
| `--primary-domain` | `string` | No | Must be in the list of domains. If there are any domains, there must be exactly one primary domain. |
| `--subaccount-ids` | `string[]` | No | An array of account IDs to be added as subaccounts to this account. For normal accounts, these represent subaccounts. For partner accounts, these represent associated accounts. |
| `--tags` | `string[]` | No | An array of strings to use as tags on this account. If provided, the accounts tags will be updated to the given tags. |

#### `pylon accounts delete`

Permanently deletes an account by ID or external ID.

**Rate limit:** 30 requests per minute

`DELETE /accounts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to delete. |

#### `pylon accounts get`

Returns a single account by ID or external ID.

**Rate limit:** 300 requests per minute

`GET /accounts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to fetch. |

#### `pylon accounts list`

Returns a paginated list of accounts for the organization.

**Rate limit:** 300 requests per minute

`GET /accounts`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of accounts to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

#### `pylon accounts list-files`

Returns the files uploaded to an account, newest first, by account ID or external ID.

**Rate limit:** 300 requests per minute

`GET /accounts/{id}/files`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account. |

#### `pylon accounts merge`

Merges one or more accounts into a surviving account. Issues, contacts, opportunities, domains, channels, external IDs, and other associated data are transferred to the surviving account. Tags and custom field values of the merged accounts are not transferred. The merged accounts are permanently deleted. This cannot be undone. Accounts are merged sequentially, each in its own transaction; if a merge fails partway through, accounts already merged are not restored.

**Rate limit:** 30 requests per minute

`POST /accounts/merge`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--merge-account-ids` | `string[]` | Yes | The IDs of the accounts to merge into the surviving account. These accounts are permanently deleted after their data is transferred. The number of accounts to merge must be between 1 and 100. |
| `--merge-into-account-id` | `string` | Yes | The ID of the account that will survive the merge and receive the merged data. |

#### `pylon accounts search`

Optionally pass `search_text` for fuzzy matching. Results are intersected with any provided filter.

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `account_id` | `equals`, `in`, `not_in`, `does_not_contain`, `is_set`, `is_unset` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last` |
 `domains` | `equals`, `contains`, `does_not_contain`, `in`, `not_in`, `string_contains`, `string_does_not_contain` |
 `external_channel_ids` | `equals`, `contains`, `does_not_contain`, `in`, `not_in` |
 `external_channel_type` | `equals`, `in`, `not_in`, `does_not_contain`, `is_set`, `is_unset` |
 `external_ids` | `equals`, `in`, `not_in`, `does_not_contain`, `is_set`, `is_unset` |
 `internal_channel_ids` | `equals`, `contains`, `does_not_contain`, `in`, `not_in` |
 `internal_slack_channel_id` | `equals`, `in`, `not_in`, `does_not_contain`, `string_contains`, `string_does_not_contain` |
 `internal_slack_channel_name` | `equals`, `in`, `not_in`, `does_not_contain`, `string_contains`, `string_does_not_contain` |
 `issue_count_last_90_days` | `equals` |
 `last_broadcast_sent_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last` |
 `last_customer_activity_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last` |
 `last_vendor_activity_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last` |
 `name` | `equals`, `in`, `not_in`, `string_contains`, `contains`, `does_not_contain` |
 `number_of_users_in_channel` | `equals` |
 `owner_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset`, `belongs_to`, `not_belongs_to`, `does_not_contain` |
 `parent_account_id` | `equals`, `in`, `not_in`, `does_not_contain`, `is_set`, `is_unset` |
 `partner_account_id` | `equals`, `in`, `not_in`, `does_not_contain`, `is_set`, `is_unset` |
 `primary_channel_id` | `equals`, `in`, `not_in`, `does_not_contain` |
 `primary_domain` | `equals`, `contains`, `does_not_contain`, `in`, `not_in`, `string_contains`, `string_does_not_contain`, `is_set`, `is_unset` |
 `slack_channel_id` | `equals`, `in`, `not_in`, `does_not_contain`, `string_contains`, `string_does_not_contain` |
 `slack_channel_name` | `equals`, `in`, `not_in`, `does_not_contain`, `string_contains`, `string_does_not_contain` |
 `source` | `equals`, `in`, `not_in`, `does_not_contain` |
 `state` | `equals`, `in`, `not_in`, `does_not_contain` |
 `tags` | `equals`, `contains`, `does_not_contain`, `in`, `not_in` |
 `type` | `equals`, `in`, `not_in`, `does_not_contain` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Filter values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

 Field | Values and behavior |
 --- | --- |
 `state` | `enabled` or `disabled`. |
 `name` | `contains` is an alias for `string_contains`. |
 `account_id` | `id` is also accepted as a field name. |
 `tags` | A tag name or ID. |

### Custom fields

Set `field` to the custom field's slug. If a custom field has the same slug as a built-in field, the custom field is matched instead, except for these fields:

`account_id`
`domains`
`tags`
`name`
`external_ids`
`owner_id`

**Rate limit:** 120 requests per minute

`POST /accounts/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of accounts to fetch. Defaults to 100. Must be between 1 and 1000. |
| `--search-text` | `string` | No | Fuzzy text search. Results are intersected with any provided filter. |
| `--sort` | `object[]` | No | The order of results, as a list of sort keys. Only one sort key is supported right now. Omit for the default order. Send the same sort with every page of a cursor. |

#### `pylon accounts update`

Updates an existing account by ID or external ID. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /accounts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-type` | `customer \| partner` | No | The type of the account. Can only be changed to "customer" or "partner". |
| `--channels` | `object[]` | No | An array of channels to be linked to this account. If provided, replaces the account's linked channels; channels you leave out are unlinked. |
| `--custom-fields` | `object[]` | No | An array of custom fields to be used on this account. |
| `--domains` | `string[]` | No | Domains of the account. Replaces the account's domains. Must specify one domain as primary. |
| `--external-ids` | `object[]` | No | An array of external IDs to be used on this account. If provided, the account's external IDs will be updated to the given external IDs. |
| `--is-disabled` | `boolean` | No | Whether the account is disabled. |
| `--logo-url` | `string` | No | Logo URL of the account. |
| `--name` | `string` | No | The name of the account. |
| `--owner-id` | `string` | No | The ID of the owner of the account. If empty string is passed in, the owner will be removed. |
| `--primary-domain` | `string` | No | Must be in the list of domains. If there are any domains, there must be exactly one primary domain. |
| `--subaccount-ids` | `string[]` | No | An array of account IDs to set as this account's subaccounts. If provided, the account's subaccounts become exactly this list; accounts you leave out are detached. |
| `--tags` | `string[]` | No | An array of strings to use as tags on this account, applied according to tags_apply_mode. By default the account's tags will be updated to the given tags. |
| `--tags-apply-mode` | `append_only \| remove_only \| replace` | No | The mode for applying tags. Valid values: "append_only", "remove_only", "replace". Defaults to "replace". |

#### `pylon accounts upload-file`

Uploads one or more files to an account by ID or external ID.

**Rate limit:** 30 requests per minute

`POST /accounts/{id}/files`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to upload files to. |

Optional multipart request body: supply the form-field flags below; binary fields accept local file paths.

Top-level multipart fields are listed below. Required indicates a required form field.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--file` | `string (binary)` | No | The file to upload. Supply a local file path. |
| `--file-url` | `string` | No | The URL to fetch the file from, if the file is not provided. |

---

### `pylon accounts activities`

#### `pylon accounts activities create`

The {id} parameter accepts either:
Internal account ID (UUID format)
External ID (any string format)

**Rate limit:** 120 requests per minute

`POST /accounts/{id}/activities`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to create the activity for. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--body-html` | `string` | No | Optional HTML content to display in the activity. |
| `--contact-id` | `string` | No | Optional contact ID of the actor of the activity. |
| `--happened-at` | `string (date-time)` | No | Timestamp (RFC3339) of when the activity happened. Defaults to the current time if empty. |
| `--link` | `string` | No | Optional link to add to the activity. |
| `--link-text` | `string` | No | Optional link text to display on the activity. Defaults to "Open link" if not provided. Applies only if a link is provided. |
| `--slug` | `string` | Yes | The slug of the activity to create. |
| `--user-id` | `string` | No | Optional user ID of the actor of the activity. |

#### `pylon accounts activities list`

Returns custom activities for the specified account, ordered from newest to oldest.
The {id} parameter accepts either:
Internal account ID (UUID format)
External ID (any string format)

**Rate limit:** 300 requests per minute

`GET /accounts/{id}/activities`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to fetch activities for. |
| `--activity-type` | `string` | No | The custom activity type slug to filter by. |
| `--start-time` | `string (date-time)` | No | The start time (RFC3339) of the activity time range. |
| `--end-time` | `string (date-time)` | No | The end time (RFC3339) of the activity time range. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of activities to fetch. Defaults to 100. Must be greater than 0 and less than or equal to 1000. |

---

### `pylon accounts email-activities`

#### `pylon accounts email-activities list`

Returns email threads synced to the specified account from connected Gmail and Outlook inboxes, ordered by their latest email from newest to oldest.
The {id} parameter accepts either:
Internal account ID (UUID format)
External ID (any string format)

**Rate limit:** 120 requests per minute

`GET /accounts/{id}/email-activities`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to fetch email activities for. |
| `--start-time` | `string (date-time)` | No | The start time (RFC3339) of the activity time range, compared against each thread's latest email. |
| `--end-time` | `string (date-time)` | No | The end time (RFC3339) of the activity time range, compared against each thread's latest email. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of email activities to fetch. Defaults to 20. Must be greater than 0 and less than or equal to 50. |

---

### `pylon accounts highlights`

#### `pylon accounts highlights create`

Creates a new highlight on an account.

**Rate limit:** 30 requests per minute

`POST /accounts/{account_id}/highlights`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--account-id` | `string` | Yes | The ID or external ID of the account that the highlight belongs to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--contact-id` | `string` | No | Optional ID or external ID of a contact to associate the resulting memory with. The contact must belong to the account. |
| `--content-html` | `string` | Yes | The HTML content for this highlight. |
| `--expires-at` | `string (date-time)` | No | Optional RFC3339 timestamp of when this highlight will expire. |

#### `pylon accounts highlights delete`

Permanently deletes an account highlight by ID.

**Rate limit:** 120 requests per minute

`DELETE /accounts/{account_id}/highlights/{highlight_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--account-id` | `string` | Yes | The ID or external ID of the account that the highlight belongs to. |
| `--highlight-id` | `string` | Yes | The ID of the highlight to delete. |

#### `pylon accounts highlights update`

Updates an existing account highlight. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /accounts/{account_id}/highlights/{highlight_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--highlight-id` | `string` | Yes | The ID of the highlight to update. |
| `--account-id` | `string` | Yes | The ID or external ID of the account that the highlight belongs to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--content-html` | `string` | No | The updated HTML content for this highlight. |
| `--expires-at` | `string` | No | The updated expires at timestamp (RFC3339). Omit it to keep the current expiry, or set it to an empty string to clear it. |

---

### `pylon accounts notebook-blocks notes`

#### `pylon accounts notebook-blocks notes create`

Creates a note in a specific Notes block in an account notebook.

**Rate limit:** 120 requests per minute

`POST /accounts/{account_id}/notebook-blocks/{block_id}/notes`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--account-id` | `string` | Yes | The ID or external ID of the account. |
| `--block-id` | `string` | Yes | The ID of the Notes block, copied from the notebook UI. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--content-html` | `string` | Yes | The note body as HTML. |
| `--title` | `string` | No | An optional title for the note. |

#### `pylon accounts notebook-blocks notes list`

Returns notes from a specific Notes block in an account notebook.

**Rate limit:** 300 requests per minute

`GET /accounts/{account_id}/notebook-blocks/{block_id}/notes`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--account-id` | `string` | Yes | The ID or external ID of the account. |
| `--block-id` | `string` | Yes | The ID of the Notes block, copied from the notebook UI. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of notes to fetch. Defaults to 20. Must be greater than 0 and less than or equal to 20. |

---

### `pylon accounts relationships`

#### `pylon accounts relationships create`

Creates a parent or partner relationship for the account in the URL.

**Rate limit:** 120 requests per minute

`POST /accounts/{account_id}/relationship`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--account-id` | `string` | Yes | The ID of the child or client account. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--related-object-id` | `string` | Yes | The ID of the related parent or partner account. |
| `--relationship-type` | `string` | Yes | The relationship type. Must be "parent_account" or "partner_account". |

#### `pylon accounts relationships delete`

Deletes an account relationship by ID.

**Rate limit:** 120 requests per minute

`DELETE /accounts/{account_id}/relationships/{relationship_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--account-id` | `string` | Yes | The ID of the child or client account. |
| `--relationship-id` | `string` | Yes | The ID of the account relationship to delete. |

#### `pylon accounts relationships list`

Returns the parent-child and partner-client relationships where the account is the child or client.

**Rate limit:** 300 requests per minute

`GET /accounts/{account_id}/relationships`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--account-id` | `string` | Yes | The ID of the child or client account whose relationships should be returned. |

---

### `pylon activity-types`

#### `pylon activity-types list`

Returns all custom activity type definitions for the organization.

**Rate limit:** 30 requests per minute

`GET /activity-types`

---

### `pylon article-feedback`

#### `pylon article-feedback list`

Returns a paginated list of knowledge base article feedback for the organization.

**Rate limit:** 120 requests per minute

`GET /article-feedback`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of feedback submissions to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |
| `--knowledge-base-id` | `string` | No | The ID of the knowledge base to filter by. |
| `--article-id` | `string` | No | The ID of the article to filter by. |

---

### `pylon attachments`

#### `pylon attachments create`

Uploads a file as an attachment. Send either `file` or `file_url` (`file` takes precedence if both are sent); one file per request. Executable and script files are rejected. The returned `url` is a signed link; pass it in `attachment_urls` when creating issues or messages. Files up to 100 MB (104,857,600 bytes) are supported. Larger files may be rejected and should be shared using an externally hosted link. This applies to direct uploads and files fetched through file_url. Downstream delivery channels may impose smaller limits.

**Rate limit:** 30 requests per minute

`POST /attachments`

Optional multipart request body: supply the form-field flags below; binary fields accept local file paths.

Top-level multipart fields are listed below. Required indicates a required form field.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--description` | `string` | No | The description of the file. |
| `--file` | `string (binary)` | No | The file to upload. Send either `file` or `file_url`; if both are sent, `file` is used and `file_url` is ignored. Files up to 100 MB (104,857,600 bytes) are supported. Larger files may be rejected and should be shared using an externally hosted link. Supply a local file path. |
| `--file-url` | `string` | No | The URL to fetch the file from. Ignored when `file` is also sent. Fetched files up to 100 MB (104,857,600 bytes) are supported. Larger files may be rejected and should be shared using an externally hosted link. |

---

### `pylon audit-logs`

#### `pylon audit-logs list`

Returns a paginated list of audit log entries for the organization.

**Rate limit:** 300 requests per minute

`GET /audit-logs`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of audit logs to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

#### `pylon audit-logs search`

Returns a filtered, paginated list of audit log entries for the organization.
Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `action` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain` |
 `action_happened_at` | `time_is_after`, `time_is_before`, `time_range` |
 `object_id` | `equals`, `in`, `not_in` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Filter values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

 Field | Values and behavior |
 --- | --- |
 `object_id` | The ID of the object the entry is for, matching `object_id` in the returned entries. |

**Rate limit:** 30 requests per minute

`POST /audit-logs/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of audit logs to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

---

### `pylon call-recordings`

#### `pylon call-recordings create`

Creates a call recording from your own call recorder. Set app_type to `custom_call_recorder`; the Custom Call Recorder integration must be enabled for your organization, or the request returns 400. start_time, end_time, and at least one call_recording_messages entry are required. Every speaker_email must appear in participant_emails or match primary_user_email. The recording is linked to account_id if provided, otherwise to an account matched from the participant emails. Reusing a recording_id returns the existing recording unchanged.

**Rate limit:** 30 requests per minute

`POST /call-recordings`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | No | The ID of the account to link this call recording to. If provided, the participant emails are not used for account matching, and an unknown ID returns 400. If omitted, Pylon matches an account from the participant emails, ignoring your organization's own domains; the recording is created without an account if none matches. |
| `--app-type` | `custom_call_recorder` | Yes | The source of the recording. Must be `custom_call_recorder`, which requires the Custom Call Recorder integration to be enabled. |
| `--call-recording-messages` | `object[]` | Yes | The transcript, one entry per utterance. `custom_call_recorder` takes its transcript only from this field and ignores a plain-text transcript. |
| `--custom-fields` | `object[]` | No | Custom fields to set on the call recording. Use slugs from GET /custom-fields?object_type=meeting. Each entry needs a slug and either value or values, not both. |
| `--end-time` | `string (date-time)` | Yes | When the call ended, in RFC3339 format (e.g. 2025-01-01T01:00:00Z). |
| `--participant-emails` | `string` | No | Comma-separated emails of everyone on the call (e.g. "alice@customer.com,bob@yourcompany.com"). Used to match the account when account_id is omitted. Every speaker_email in call_recording_messages must be in this list or match primary_user_email. |
| `--primary-user-email` | `string` | No | The email of the Pylon user who owns the recording. Counted as a participant, so it does not need to be repeated in participant_emails. |
| `--recording-id` | `string` | No | Your unique ID for this recording. Pylon deduplicates on recording_id and app_type: a request that reuses a recording_id returns the existing recording unchanged. Send a unique value for every call; if you omit it, every request after the first returns the same recording. |
| `--recording-url` | `string` | No | A link to the recording in your call recorder. Maximum 255 characters. |
| `--start-time` | `string (date-time)` | Yes | When the call started, in RFC3339 format (e.g. 2025-01-01T00:00:00Z). |
| `--title` | `string` | No | The title of the call recording. |

#### `pylon call-recordings delete`

Permanently deletes a call recording by its Pylon ID.

**Rate limit:** 120 requests per minute

`DELETE /call-recordings/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The Pylon ID of the call recording to delete. |

#### `pylon call-recordings get`

Returns a single call recording by ID.

**Rate limit:** 300 requests per minute

`GET /call-recordings/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the call recording to fetch. |

#### `pylon call-recordings search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `account_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `source` | `equals`, `in`, `not_in` |
 `title` | `equals`, `string_contains` |
 `start_time` | `time_is_after`, `time_is_before`, `time_range` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Timestamp values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

**Rate limit:** 120 requests per minute

`POST /call-recordings/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of call recordings to fetch. Defaults to 100. Must be greater than 0 and less than or equal to 1000. |

#### `pylon call-recordings update`

Updates a call recording by ID. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /call-recordings/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the call recording to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | No | The account ID to associate with the call recording. Pass an empty string to remove the account association. |
| `--custom-fields` | `object[]` | No | An array of custom fields to set on the call recording. Only passed in fields will be modified. |

---

### `pylon contacts`

#### `pylon contacts create`

Creates a new contact with the specified email and optional metadata.

**Rate limit:** 300 requests per minute

`POST /contacts`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-external-id` | `string` | No | The external ID of the account that this contact belongs to. Cannot be used together with account_id. |
| `--account-id` | `string` | No | The account that this contact belongs to. |
| `--avatar-url` | `string` | No | The avatar URL of the contact. Must be a square .png, .jpg or .jpeg. |
| `--custom-fields` | `object[]` | No | An array of custom fields to be applied to this contact. |
| `--email` | `string` | No | The email of the contact. |
| `--external-ids` | `object[]` | No | An array of external IDs to be used on this contact. |
| `--name` | `string` | Yes | The name of the contact. |
| `--phone-numbers` | `string[]` | No | The phone numbers of the contact. Must contain only digits 0-9, optionally preceded by + (E.164, e.g. +4365446231), and be 15 digits or less. Include the + and country code for non-US numbers; a 10-digit number without + is treated as US. |
| `--portal-role` | `string` | No | The portal role to assign to the contact. If not provided uses the default portal role from the portal settings.  Known values: `no_access`, `member`, `admin`. This list is not exhaustive. |
| `--portal-role-id` | `string` | No | The ID of the custom portal role to assign to the contact. Takes precedence over portal_role if provided. |
| `--primary-phone-number` | `string` | No | The primary phone number. Must be in the list of phone_numbers. If there are any phone_numbers and this is not specified, the first phone number will be primary. |

#### `pylon contacts delete`

Permanently deletes a contact by ID or external ID.

**Rate limit:** 30 requests per minute

`DELETE /contacts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the contact to delete. |

#### `pylon contacts get`

Returns a single contact by ID or external ID.

**Rate limit:** 300 requests per minute

`GET /contacts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the contact. |

#### `pylon contacts list`

Returns a paginated list of contacts for the organization.

**Rate limit:** 300 requests per minute

`GET /contacts`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of contacts to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

#### `pylon contacts merge`

Merges a contact into a surviving contact. Both contacts must belong to the same account, unless the merged contact has no account, in which case it is first moved to the surviving contact's account. Issues, emails, phone numbers, survey responses, and other associated data are then transferred to the surviving contact, and the merged contact is permanently deleted. This cannot be undone.

**Rate limit:** 30 requests per minute

`POST /contacts/merge`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--merge-contact-id` | `string` | Yes | The ID of the contact to merge into the surviving contact. This contact is permanently deleted after its data is transferred. |
| `--merge-into-contact-id` | `string` | Yes | The ID of the contact that will survive the merge and receive the merged data. If the merged contact belongs to an account, this contact must belong to the same account. |

#### `pylon contacts portal-invitation`

Sends or resends a portal invitation to the contact's primary email. The portal must be enabled and the contact must already have portal access. Does not change the contact's role. Requires customer portal settings write permission and write access to the contact's primary account, if any. Each successful call requests another invitation; success does not guarantee email delivery.

**Rate limit:** 30 requests per minute

`POST /contacts/{id}/portal-invitation`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the contact to invite. |

#### `pylon contacts search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `id` | `equals`, `in`, `not_in` |
 `email` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain` |
 `name` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain` |
 `account_id` | `equals`, `in`, `not_in` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Custom fields

Set `field` to the custom field's slug.

**Rate limit:** 120 requests per minute

`POST /contacts/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of contacts to fetch. Defaults to 100. Must be between 1 and 1000. |
| `--search-text` | `string` | No | Text search across contact name, primary email, secondary emails, primary phone number, and secondary phone numbers. Results are intersected with any provided filter. |

#### `pylon contacts update`

Updates a contact by ID or external ID. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /contacts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the contact to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-external-id` | `string` | No | The external ID of the account to move the contact to. Cannot be used together with account_id. |
| `--account-id` | `string` | No | The account to move the contact to. If empty string is passed in, the contact will be removed from its account. |
| `--avatar-url` | `string` | No | The avatar URL of the contact. Must be a square .png, .jpg or .jpeg. |
| `--custom-fields` | `object[]` | No | An array of custom fields to be applied to this contact. |
| `--email` | `string` | No | The email of the contact. Replaces all of the contact's emails with this single email. Cannot be used together with the `emails` array field. |
| `--emails` | `object[]` | No | The emails of the contact as an array. Cannot be used together with the singular `email` field. Each entry must include an `email` string and an optional `is_primary` boolean. If no email is marked as primary, the first email becomes the primary. |
| `--external-ids` | `object[]` | No | An array of external IDs to be used on this contact. If provided, the contact's external IDs will be updated to the given external IDs. |
| `--name` | `string` | No | in: body The name of the contact. |
| `--phone-numbers` | `string[]` | No | The phone numbers of the contact. Must contain only digits 0-9, optionally preceded by + (E.164, e.g. +4365446231), and be 15 digits or less. Include the + and country code for non-US numbers; a 10-digit number without + is treated as US. |
| `--portal-role` | `string` | No | The portal role to assign to the contact. Can be one of `no_access`, `member`, or `admin`, or a custom role slug.  Known values: `no_access`, `member`, `admin`. This list is not exhaustive. |
| `--portal-role-id` | `string` | No | The ID of the custom portal role to assign to the contact. Takes precedence over portal_role if provided. |
| `--primary-phone-number` | `string` | No | The primary phone number. Must be in the list of phone_numbers. If there are any phone_numbers and this is not specified, the first phone number will be primary. |

---

### `pylon custom-fields`

#### `pylon custom-fields create`

Creates a new custom field definition for the specified object type.

**Rate limit:** 120 requests per minute

`POST /custom-fields`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--default-value` | `string` | No | The default value for single-valued custom fields. |
| `--default-values` | `string[]` | No | The default values for multi-valued custom fields. |
| `--description` | `string` | No | The description of the custom field. |
| `--instructions` | `string` | No | Field-wide instructions for how AI should populate the field. For AI-enabled fields, an empty value falls back to description. |
| `--is-ai-enabled` | `boolean` | No | Whether AI should populate the field. Web research fields are always AI-enabled. |
| `--json-schema` | `string` | No | JSON schema for structured web research results. Required for contact web research fields. |
| `--label` | `string` | Yes | The label of the custom field. |
| `--object-type` | `account \| issue \| contact \| task \| project \| meeting \| opportunity \| feature_request` | Yes | The object type of the custom field. Can be "account", "issue", "contact", "task", "project", "meeting", "opportunity", or "feature_request". |
| `--select-options` | `object[]` | No | The list options of the select custom field. This is only present for select and multiselect custom fields. |
| `--slug` | `string` | No | The slug of the custom field. |
| `--type` | `string` | Yes | The type of the custom field. Can be one of `text`, `number`, `boolean`, `date`, `datetime`, `user`, `url`, `select`, `multiselect`, or `web_research`. Number fields accept integers and fractional values, such as 7.4; decimal is not a separate field type. Web research is supported for accounts and for contacts when enabled for the organization. |

#### `pylon custom-fields get`

Returns a single custom field definition by ID.

**Rate limit:** 300 requests per minute

`GET /custom-fields/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the custom field. |

#### `pylon custom-fields list`

Returns all custom field definitions for the specified object type. Use `slug` (and `select_metadata.options[].slug` for option values) in API writes and filters.

**Rate limit:** 300 requests per minute

`GET /custom-fields`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--object-type` | `account \| issue \| contact \| task \| project \| meeting \| opportunity \| feature_request` | Yes | The object type of the custom fields. Can be "account", "issue", "contact", "task", "project", "meeting", "opportunity", or "feature_request". |

#### `pylon custom-fields update`

Updates a custom field definition. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /custom-fields/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the custom field. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--add-select-options` | `object[]` | No | Options to add without replacing existing options or changing existing labels and AI criteria. Cannot be combined with select_options. |
| `--default-value` | `string` | No | The default value for single-valued custom fields. |
| `--default-values` | `string[]` | No | The default values for multi-valued custom fields. |
| `--description` | `string` | No | The description of the custom field. |
| `--instructions` | `string` | No | Field-wide instructions for how AI should populate the field. An empty string clears saved instructions when AI is disabled. |
| `--is-ai-enabled` | `boolean` | No | Whether AI should populate the field. Omit to preserve the current setting. |
| `--label` | `string` | No | The label of the custom field. |
| `--option-descriptions` | `object` | No | AI selection criteria keyed by exact option slug. Omitted options are preserved; an empty string clears an option's criteria. |
| `--requirement` | `object` | No |  |
| `--select-options` | `object[]` | No | The complete list of options for a select or multiselect custom field. Options missing from the list are deleted and their stored values are cleared asynchronously. Prefer the dedicated select option endpoints, which can rename an option without losing stored values. |
| `--slug` | `string` | No | The slug of the custom field. |
| `--visible-by-default` | `boolean` | No | Whether the custom field shows on records in Pylon by default. When false, it shows only where a field visibility condition makes it visible. Omit to keep the current setting. |

---

### `pylon custom-fields select-options`

#### `pylon custom-fields select-options create`

Adds an option to a select or multiselect custom field.

**Rate limit:** 120 requests per minute

`POST /custom-fields/{id}/select-options`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the custom field. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--ai-description` | `string` | No | The AI description used to help AI-enabled fields select this option. |
| `--label` | `string` | Yes | The display label of the option. |
| `--slug` | `string` | Yes | The API slug stored as the option value. |

#### `pylon custom-fields select-options delete`

Deletes an option and asynchronously clears it from affected objects.

**Rate limit:** 120 requests per minute

`DELETE /custom-fields/{id}/select-options`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the custom field. |
| `--current-slug` | `string` | Yes | The current option slug. |

#### `pylon custom-fields select-options update`

Updates an option's slug, label, or AI description. Slug changes preserve existing values and migrate persisted filters.

**Rate limit:** 120 requests per minute

`PATCH /custom-fields/{id}/select-options`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the custom field. |
| `--current-slug` | `string` | Yes | The current option slug. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--ai-description` | `string` | No | A replacement AI description. Pass an empty string to clear it. |
| `--label` | `string` | No | A replacement display label. |
| `--slug` | `string` | No | A replacement API slug. Existing object values and persisted filters are migrated to this slug. |

---

### `pylon custom-objects`

#### `pylon custom-objects bulk-update`

Applies the same update to multiple custom objects of the given type in a single request. Pass between 1 and 100 IDs and the custom field values to set; only the provided fields are modified on each object. To update the linked account, pass the built-in Account relationship field in `custom_fields`: `{"ids":["object_uuid"],"custom_fields":{"account":{"value":"account_uuid"}}}`. To unset a field, pass its slug with an empty value.

**Rate limit:** 120 requests per minute

`PATCH /custom-objects/{type}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "opportunity"). |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--custom-fields` | `object` | No | Custom field values to apply to every listed custom object, keyed by field slug. To unset a field, pass its slug with an empty value. |
| `--ids` | `string[]` | Yes | The IDs of the custom objects to update. Must be between 1 and 100 IDs. |

#### `pylon custom-objects create`

Creates a new custom object instance of the given type. To link the object to an account, pass the built-in Account relationship field in `custom_fields`: `{"name":"Example","custom_fields":{"account":{"value":"account_uuid"}}}`.

**Rate limit:** 120 requests per minute

`POST /custom-objects/{type}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--custom-fields` | `object` | No | Custom field values to set on the object, keyed by field slug. To link the object to an account, pass the built-in Account relationship field as `custom_fields.account.value`, for example `{"custom_fields":{"account":{"value":"account_uuid"}}}`. |
| `--name` | `string` | Yes | The name of the custom object. |

#### `pylon custom-objects delete`

Deletes a custom object instance.

**Rate limit:** 120 requests per minute

`DELETE /custom-objects/{type}/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |
| `--id` | `string` | Yes | The ID of the custom object. |

#### `pylon custom-objects get`

Returns a single custom object by ID, including its custom field values.

**Rate limit:** 300 requests per minute

`GET /custom-objects/{type}/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |
| `--id` | `string` | Yes | The ID of the custom object. |

#### `pylon custom-objects list`

Returns paginated custom objects of the given type.

**Rate limit:** 300 requests per minute

`GET /custom-objects/{type}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |
| `--cursor` | `string` | No | Pagination cursor for the next page. |
| `--limit` | `integer (int64)` | No | Number of results per page. Defaults to 25, max 100. |

#### `pylon custom-objects search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `name` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain`, `is_set`, `is_unset` |
 `account` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Filter values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

 Field | Values and behavior |
 --- | --- |
 `account` | The built-in Account relationship field on every custom object type. Use account IDs as values. |

### Custom fields

Set `field` to the custom field's slug.

### Opportunities

A `{type}` of `opportunity` is an alias for the opportunities API and filters on a different set of fields:

 Field | Allowed operators |
 --- | --- |
 `name` | `equals`, `in`, `not_in`, `string_contains` |
 `account_id` | `equals`, `in`, `not_in` |
 `source` | `equals`, `in`, `not_in` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |

**Rate limit:** 120 requests per minute

`POST /custom-objects/{type}/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of results to fetch. Defaults to 25, max 100. |

#### `pylon custom-objects update`

Updates a custom object. Only provided fields are modified. To update the linked account, pass the built-in Account relationship field in `custom_fields`: `{"custom_fields":{"account":{"value":"account_uuid"}}}`.

**Rate limit:** 120 requests per minute

`PATCH /custom-objects/{type}/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |
| `--id` | `string` | Yes | The ID of the custom object. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--custom-fields` | `object` | No | Custom field values to set on the object, keyed by field slug. To update the linked account, pass the built-in Account relationship field as `custom_fields.account.value`, for example `{"custom_fields":{"account":{"value":"account_uuid"}}}`. |
| `--name` | `string` | No | The name of the custom object. |

---

### `pylon email-suppressions`

#### `pylon email-suppressions delete`

Removes the suppression so Pylon resumes sending email to the address.

**Rate limit:** 120 requests per minute

`DELETE /email-suppressions/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the email suppression to remove. |

#### `pylon email-suppressions list`

Returns the email addresses Pylon will not send to, most recently suppressed first. Pass `email` to check a single address; an empty `data` array means it is not suppressed.

**Rate limit:** 300 requests per minute

`GET /email-suppressions`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--email` | `string` | No | Only return the suppression for this email address, if one exists. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of suppressions to fetch. Defaults to 100. Must be greater than 0 and less than or equal to 1000. |

---

### `pylon feature-requests`

#### `pylon feature-requests add-evidence`

Creates a manual evidence record linking a customer account to a feature request. Repeated requests create separate evidence records.

**Rate limit:** 120 requests per minute

`POST /feature-requests/{id}/evidence`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request. |

Required request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | Yes | The ID of the customer account to link to the feature request. |
| `--summary` | `string` | No | A summary explaining why this account is linked. Defaults to "Account manually linked via API." |

#### `pylon feature-requests create`

Creates a new feature request. When should_auto_fetch_evidence is true, supporting evidence is automatically gathered and used to generate the description.

**Rate limit:** 120 requests per minute

`POST /feature-requests`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--description` | `string` | No | The description of the feature request. Ignored when should_auto_fetch_evidence is true, since the description is then generated from gathered evidence. |
| `--should-auto-fetch-evidence` | `boolean` | No | When true, asynchronously gathers supporting evidence and generates a description, mirroring the in-app experience. Defaults to false, which creates the feature request as-is. |
| `--title` | `string` | Yes | The title of the feature request. |

#### `pylon feature-requests delete`

Permanently deletes a feature request and its associated evidence.

**Rate limit:** 120 requests per minute

`DELETE /feature-requests/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request to delete. |

#### `pylon feature-requests get`

Returns a single feature request by ID. Optionally includes evidence items when fetch_evidence is true.

**Rate limit:** 300 requests per minute

`GET /feature-requests/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request to fetch. |
| `--fetch-evidence` | `boolean` | No | Whether to include evidence items in the response. Defaults to false. |

#### `pylon feature-requests link-external-issue`

By default, links the external issue and creates a backlink to the feature request in the source system. To unlink it, set the operation field to "unlink". Repeating the same link request is a successful no-op.

**Rate limit:** 120 requests per minute

`POST /feature-requests/{id}/external-issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request to link an external issue to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--external-issue-id` | `string` | Yes | The ID or human-readable key of the external issue in the source system. |
| `--operation` | `string` | No | Operation to perform. Use "link" to link the issue (default) or "unlink" to unlink it. |
| `--source` | `string` | Yes | The source system of the external issue (e.g., "linear", "asana", "jira", "github", "shortcut"). |

#### `pylon feature-requests merge`

Merges one or more feature requests into a surviving feature request. Evidence and linked external issues are consolidated, and merged feature requests are archived. Merge requests that share a target should be sent serially.

**Rate limit:** 30 requests per minute

`POST /feature-requests/merge`

Required request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--merge-feature-request-ids` | `string[]` | Yes | The IDs of the Feature Requests to merge into the surviving Feature Request. Must contain between 1 and 100 unique IDs. |
| `--merge-into-feature-request-id` | `string` | Yes | The ID of the Feature Request that will survive the merge. |

#### `pylon feature-requests search`

Returns feature requests matching the given criteria. Supports semantic search, status filtering, and pagination.

**Rate limit:** 120 requests per minute

`POST /feature-requests/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-ids` | `string[]` | No | Filter by one or more account IDs. Returns only feature requests with evidence linked to any of the given accounts. |
| `--limit` | `integer (int64)` | No | The maximum number of feature requests to return. Defaults to 100, max 1000. |
| `--query` | `string` | No | A search query string for semantic and keyword matching. If omitted, all feature requests are returned (subject to other filters and limit). |
| `--request-statuses` | `string[]` | No | Filter by one or more request statuses. Each value can be a built-in status (new, in_progress, closed, archived) or a custom status slug. |

#### `pylon feature-requests set-portal-visibility`

Toggles portal visibility for a set of accounts on a feature request. Idempotent — adding already-visible accounts or removing already-hidden accounts is a no-op. Note: visibility only takes effect when the Feature Requests tab is enabled in portal settings.

**Rate limit:** 120 requests per minute

`POST /feature-requests/{id}/set-portal-visibility`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-ids` | `string[]` | Yes | The account IDs to add or remove portal visibility for. |
| `--visible` | `boolean` | Yes | Whether the specified accounts should be able to see this feature request in the portal. True to add visibility, false to remove. |

#### `pylon feature-requests update`

Updates an existing feature request. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /feature-requests/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--custom-fields` | `object[]` | No | An array of custom fields to set. Only passed-in fields will be modified. |
| `--request-status` | `string` | No | The new request status. Can be a built-in status (new, in_progress, closed, archived) or a custom status slug. |

---

### `pylon issue-groups`

#### `pylon issue-groups create`

Creates an issue group and attaches its initial child issues atomically.

**Rate limit:** 30 requests per minute

`POST /issue-groups`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--child-issue-ids` | `string[]` | Yes | The IDs of the issues to include in the group. At least one is required. |
| `--title` | `string` | Yes | The title of the issue group. |

---

### `pylon issue-groups children`

#### `pylon issue-groups children add`

Adds one or more child issues atomically. Issues already attached to this group are ignored.

**Rate limit:** 120 requests per minute

`POST /issue-groups/{issue_group_id}/children`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--issue-group-id` | `string` | Yes | The ID of the issue group. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--child-issue-ids` | `string[]` | Yes | The IDs of the issues to add to the group. At least one is required. |

#### `pylon issue-groups children remove`

Removes one child issue. An issue group must retain at least one child.

**Rate limit:** 120 requests per minute

`DELETE /issue-groups/{issue_group_id}/children/{child_issue_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--issue-group-id` | `string` | Yes | The ID of the issue group. |
| `--child-issue-id` | `string` | Yes | The ID of the child issue to remove. |

---

### `pylon issue-statuses`

#### `pylon issue-statuses list`

Returns all issue statuses for the organization. Use `slug` as `state` in PATCH /issues and issue search filters.

**Rate limit:** 30 requests per minute

`GET /issue-statuses`

---

### `pylon issues`

#### `pylon issues bulk-update`

Applies the same changes to up to 100 issues. Only provided fields are modified. Issues that do not exist, or that the caller cannot update, are skipped and listed in skipped_issues instead of failing the request.

**Rate limit:** 30 requests per minute

`PATCH /issues`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--assignee-id` | `string` | No | The ID of the user to assign the issues to. If empty string is passed in, the issues will be unassigned. |
| `--custom-fields` | `object[]` | No | Custom fields to set on the issues. Only passed in fields are modified. Clearing a custom field is not supported in bulk; use PATCH /issues/{id}. |
| `--customer-portal-visible` | `boolean` | No | Whether the issues should be visible in the customer portal. |
| `--issue-ids` | `string[]` | Yes | The IDs of the issues to update. Must contain between 1 and 100 IDs. |
| `--state` | `string` | No | The state to move the issues to. Standard values are `new`, `waiting_on_you`, `waiting_on_customer`, `on_hold`, and `closed`; custom status slugs are also supported. |
| `--tags` | `string[]` | No | Tags to apply to the issues, according to tags_apply_mode. |
| `--tags-apply-mode` | `append_only \| remove_only \| replace` | No | The mode for applying tags. Valid values: "append_only", "remove_only", "replace". Defaults to "replace". |
| `--team-id` | `string` | No | The ID of the team to assign the issues to. If empty string is passed in, the team will be removed. Team assignment is applied asynchronously. |

#### `pylon issues create`

Creates a new issue and its first message. Requires either an account_id or requester information.

Requester fields identify the customer, user_id or contact_id identifies the first-message author, and destination_metadata controls delivery. These choices are independent. If destination_metadata is omitted, the first message is an internal note and no customer is contacted. See the request-field descriptions and examples for destination-specific requirements.

**Rate limit:** 30 requests per minute

`POST /issues`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | No | The account that this issue belongs to. If requester_id is also provided, the requester must belong to this account. If requester_email is provided, the contact is found or created in this account. |
| `--assignee-id` | `string` | No | The user the issue should be assigned to. |
| `--attachment-urls` | `string[]` | No | URLs of files to attach to the issue's first message. |
| `--author-unverified` | `boolean` | No | Whether the requester's identity has NOT been verified. Defaults to false (verified). |
| `--body-html` | `string` | Yes | The HTML content of the body of the issue. |
| `--contact-id` | `string` | No | The contact to attribute the first message to. This controls the message author, not the issue requester. Makes the message appear as a customer message rather than an internal note. Only one of user_id or contact_id can be provided. Requires destination_metadata. |
| `--created-at` | `string (date-time)` | No | Timestamp of when the issue was created. If not specified, the current time will be used. (RFC3339) |
| `--custom-fields` | `object[]` | No | An array of custom fields to be used on this issue. |
| `--custom-issue-source-id` | `string` | No | The ID of a custom issue source (created in the App Directory under Chat > Add Custom Chat App). Sets the issue source to the custom source's slug. Use this for channels Pylon doesn't natively support (e.g. WeChat). Cannot be combined with destination_metadata. |
| `--customer-portal-visible` | `boolean` | No | Whether the issue should be visible in the customer portal. When destination is "customer_portal", this is set to true and cannot be false. |
| `--destination-metadata` | `object` | No | Specifies if/how communication will be delivered to the customer. You can configure the issue to contact the requester via email, Slack, in-app chat, SMS, WhatsApp, make it available only in the customer portal, or keep it internal. If an external destination is specified, a message with the issue's BodyHTML will be delivered to the requester. The `customer_portal` destination requires Customer Portal to be enabled and creates a customer-visible message without external delivery. To avoid contacting the requester, omit destination_metadata from the create-issue request or specify the `internal` destination. If destination_metadata is provided, destination is required. |
| `--priority` | `urgent \| high \| medium \| low` | No | The priority of the issue. Can be one of: urgent, high, medium, or low. |
| `--requester-avatar-url` | `string` | No | The URL of an avatar of the requester. |
| `--requester-email` | `string` | No | The email of the customer this issue is for. Used when requester_id is omitted. If no matching contact exists, one will be created. When account_id is provided, the contact is found or created in that account. This does not control who authored the first message. |
| `--requester-id` | `string` | No | The customer this issue is for. Sets the "Requester" shown in the issue sidebar but does not control who authored the first message. If account_id is omitted, the requester's primary account is used when available. If requester_email is also provided, requester_id takes precedence. |
| `--requester-name` | `string` | No | The optional full name of the requester. Used when creating a new contact via requester_email. |
| `--requester-phone-number` | `string` | No | The phone number of a new requester. Only supported for direct WhatsApp delivery and cannot be combined with requester_id, requester_email, requester_name, or requester_avatar_url. The number is normalized to E.164 format and used to create a phone-only contact in the same transaction as the issue. |
| `--tags` | `string[]` | No | An array of strings to use as tags on this issue. If provided, the issue tags will be updated to the given tags. |
| `--team-id` | `string` | No | The ID of the team this issue should be assigned to. |
| `--title` | `string` | Yes | The title of the issue. |
| `--user-id` | `string` | No | The internal Pylon user to attribute the first message to. This does not assign the user as the requester. Only one of user_id or contact_id can be provided. If neither is set, the API token's user is used. |

#### `pylon issues create-ai-response`

Generates an AI response for the specified issue using the given agent.

**Rate limit:** 120 requests per minute

`POST /issues/{id}/ai-response`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to create an AI response for. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--ai-agent-id` | `string` | Yes | The ID of the AI agent to use to create the AI response. |
| `--post-as-internal-note` | `boolean` | No | Whether to post the AI response as an internal note on the issue. |

#### `pylon issues create-draft-reply`

Creates a private customer-reply draft without sending it. The draft is visible only to its owner and may require a normal issue refetch before appearing in the app. For unlinked or service API tokens, user_id is required. This endpoint updates only untouched drafts that it previously created; every other existing draft returns a conflict.

**Rate limit:** 30 requests per minute

`POST /issues/{id}/draft-reply`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue. |

Required request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--bcc-emails` | `string[]` | No | The draft's BCC recipients. See to_emails. |
| `--body-html` | `string` | Yes | The draft body in HTML. |
| `--cc-emails` | `string[]` | No | The draft's CC recipients. See to_emails. |
| `--to-emails` | `string[]` | No | The draft's To recipients. If any of to_emails, cc_emails, or bcc_emails is provided, the draft uses exactly those lists and an omitted list is saved empty; omit all three to use the composer's default recipients. |
| `--user-id` | `string` | No | The active Pylon user who should own and see the draft. Defaults to the API-token user when it is a human Pylon user; required for unlinked or service API tokens. |

#### `pylon issues create-note`

Posts an internal note on an issue thread. Not visible to the requester.

Thread selection:
* If thread_id is provided, posts to that internal thread.
* If message_id is provided, posts to the thread containing that internal note.
* Providing both thread_id and message_id returns a 400 response.
* If neither is provided, posts to the most recently created Slack-backed internal thread. If none exists, creates a Pylon-only internal thread.
* thread_name names that newly created Pylon-only thread and is otherwise ignored.

Empty thread_id, message_id, and thread_name values are treated as omitted.

**Rate limit:** 30 requests per minute

`POST /issues/{id}/note`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--attachment-urls` | `string[]` | No | URLs of files to attach to this internal note. |
| `--body-html` | `string` | Yes | The body of the message in HTML. |
| `--message-id` | `string` | No | The ID of an internal note whose thread should receive the new note. Use the top-level `id` from GET /issues/{id}/messages. Cannot be combined with thread_id. |
| `--thread-id` | `string` | No | The ID of the internal thread to post the note to. Use the `id` field (not `thread_id`) from GET /issues/{id}/threads. Cannot be combined with message_id. |
| `--thread-name` | `string` | No | Optional name for a new Pylon-only internal thread. Used only when neither thread_id nor message_id is provided and no Slack-backed internal thread exists. |
| `--user-id` | `string` | No | Optional user ID to post the message as. If not provided, the API token user will be used. |

#### `pylon issues delete`

Permanently deletes an issue by ID.

**Rate limit:** 120 requests per minute

`DELETE /issues/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to delete. |

#### `pylon issues get`

Returns a single issue by ID or issue number.

**Rate limit:** 300 requests per minute

`GET /issues/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to fetch. |

#### `pylon issues link-external-incident`

Links an incident from one of the organization's connected incident systems (incident.io or Rootly). An issue can have several linked incidents, and linking one that is already linked has no effect. To unlink, set the operation field to "unlink".

**Rate limit:** 120 requests per minute

`POST /issues/{id}/external-incidents`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to link the incident to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--incident-id` | `string` | Yes | The incident's reference (such as INC-123 or ROOT-123) or its ID in the incident system. |
| `--operation` | `string` | No | Operation to perform. Use "link" to link the incident (default) or "unlink" to unlink it. |
| `--source` | `incident_io \| rootly` | Yes | The incident system the incident belongs to. It must be connected to the organization. Valid values: "incident_io", "rootly" |

#### `pylon issues link-external-issue`

By default, links external issues. To unlink issues, set the operation field to "unlink".

**Rate limit:** 120 requests per minute

`POST /issues/{id}/external-issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to link external issues to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--external-issue-id` | `string` | Yes | The ID of the external issue in the source system. |
| `--operation` | `string` | No | Operation to perform. Use "link" to link issues (default) or "unlink" to unlink issues. |
| `--source` | `string` | Yes | The source system of the external issue (e.g., "linear", "asana", "jira", "github", "shortcut"). |

#### `pylon issues list`

Returns a paginated list of issues created within a required time range (max 365 days). Results are sorted by created_at, newest first. To filter on updated_at or other timestamps, use POST /issues/search.

**Rate limit:** 30 requests per minute

`GET /issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--start-time` | `string (date-time)` | Yes | The start of the time range, filtering on the issue's created_at (inclusive). Use RFC3339 with Z or a URL-encoded offset (%2B). The duration between start_time and end_time must be less than or equal to 365 days. |
| `--end-time` | `string (date-time)` | Yes | The end of the time range, filtering on the issue's created_at (exclusive). Use RFC3339 with Z or a URL-encoded offset (%2B). The duration between start_time and end_time must be less than or equal to 365 days. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of issues to fetch. Defaults to 20000. Set to 0 or omit to use the default. Must be between 0 and 20000. |

#### `pylon issues mark-spam`

Marks up to 100 email issues as spam. Each issue is deleted, and the sender's email address is blocked unless it belongs to your own domains or support inboxes. If an issue's account has no issues left afterwards, the account is deleted too. Issues from other sources are skipped with reason unsupported_source. Issues that do not exist, or that the caller cannot mark as spam, are skipped and listed in skipped_issues instead of failing the request.

**Rate limit:** 30 requests per minute

`POST /issues/mark-spam`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--issue-ids` | `string[]` | Yes | The IDs of the issues to mark as spam. Must contain between 1 and 100 IDs. |

#### `pylon issues merge`

Merges one or more issues into a primary issue. All issues must belong to the same account (or, without an account, the same requester). All issues are found and validated before anything changes, so a request rejected for a missing or ineligible issue merges nothing. Closing messages are sent before the merge and are not recalled: if sending one fails, or the merge fails afterwards, duplicates processed earlier may already have received it. This cannot be undone.

**Rate limit:** 30 requests per minute

`POST /issues/merge`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--closing-message` | `string` | No | Optional plain-text message sent to the customer on each merged Slack or form issue before it is merged. |
| `--duplicate-issue-ids` | `string[]` | Yes | The IDs or numbers of the issues to merge into the primary issue. Must contain between 1 and 50 issues, all in the same account as the primary issue. |
| `--primary-issue-id` | `string` | Yes | The ID or number of the issue to merge into. It keeps its ID and receives the messages of the merged issues. |

#### `pylon issues reply`

Sends a customer-facing reply on an issue, visible to the requester.

message_id is required to identify which existing customer-visible conversation or thread to continue. Use the top-level message id returned by GET /issues/{id}/messages; do not use an external provider's message ID or the nested email_info.message_id value.

For an email conversation, email_info must contain at least one recipient across to_emails, cc_emails, and bcc_emails. The referenced message controls email threading, but its recipients are not copied automatically.

**Rate limit:** 30 requests per minute

`POST /issues/{id}/reply`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--attachment-urls` | `string[]` | No | URLs of files to attach to this reply. |
| `--body-html` | `string` | Yes | The body of the message in HTML. |
| `--contact-id` | `string` | No | Optional contact ID to post the message as. Only one of user_id or contact_id can be provided. |
| `--custom-source` | `object` | No |  |
| `--email-info` | `object` | No | Recipient information for replies to email conversations. Provide at least one address across to_emails, cc_emails, and bcc_emails. Recipients are not inferred from the referenced message. |
| `--message-id` | `string` | Yes | The top-level Pylon message ID to reply to, from the `id` field returned by GET /issues/{id}/messages. The message must belong to the issue in the request path and must be customer-visible, not an internal note. This selects the external conversation or thread where the reply is delivered. For email, it also sets the In-Reply-To and References chain. Do not use a provider-specific message ID or email_info.message_id. |
| `--user-id` | `string` | No | Optional user ID to post the message as. Only one of user_id or contact_id can be provided. |

#### `pylon issues search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `account_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `customer_portal_visible` | `equals`, `in`, `not_in` |
 `ticket_form_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `requester_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `follower_user_id` | `equals`, `in`, `not_in` |
 `follower_contact_id` | `equals`, `in`, `not_in` |
 `state` | `equals`, `in`, `not_in` |
 `tags` | `contains`, `does_not_contain`, `in`, `not_in`, `includes_exactly` |
 `subject` | `string_contains`, `string_does_not_contain` |
 `body_html` | `string_contains`, `string_does_not_contain` |
 `assignee_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset`, `belongs_to`, `not_belongs_to` |
 `team_id` | `equals`, `in`, `not_in` |
 `issue_type` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `issue_is_issue_group` | `equals`, `in`, `not_in` |
 `resolved_at` | `time_is_after`, `time_is_before`, `time_range` |
 `latest_message_activity_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |
 `slack_channel_id` | `equals`, `in`, `not_in` |
 `workspace_email` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `reopened` | `equals`, `in`, `not_in` |
 `number` | `equals`, `in`, `not_in` |
 `source` | `equals`, `in`, `not_in` |
 `first_response_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last`, `is_set`, `is_unset` |
 `latest_customer_message_activity_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last`, `is_set`, `is_unset` |
 `latest_vendor_message_activity_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last`, `is_set`, `is_unset` |
 `partner_account_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `is_snoozed` | `equals`, `in`, `not_in` |
 `requester_email` | the operators of the requester's `email` |
 `parent_issue_group_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `number_of_touches` | `equals`, `greater_than`, `greater_than_or_equals`, `less_than`, `less_than_or_equals` |
 `email_subject` | `string_contains`, `string_does_not_contain`, `starts_with`, `ends_with`, `is_set`, `is_unset` |
 `first_message_from` | `equals`, `in`, `not_in`, `is_set` |
 `last_message_from` | `equals`, `in`, `not_in`, `is_set` |
 `latest_public_message_activity_at` | `time_is_after`, `time_is_before`, `time_range`, `time_is_in_last`, `time_is_not_in_last`, `is_set`, `is_unset` |
 `number_of_customer_messages` | `equals`, `greater_than`, `greater_than_or_equals`, `less_than`, `less_than_or_equals`, `is_set`, `is_unset` |
 `message_redaction_used` | `equals`, `in`, `not_in` |
 `time_to_first_response` | `greater_than`, `greater_than_or_equals`, `less_than`, `less_than_or_equals`, `is_set` |
 `from_email` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain`, `starts_with`, `ends_with`, `is_set` |
 `cc_email` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain`, `starts_with`, `ends_with`, `is_set`, `is_unset` |
 `ccs` | `equals`, `in`, `not_in`, `string_contains`, `string_does_not_contain`, `starts_with`, `ends_with`, `is_set`, `is_unset` |
 `asana_product_issue` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `github_product_issue` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `jira_product_issue` | `equals`, `in`, `not_in`, `string_contains`, `starts_with`, `ends_with`, `is_set`, `is_unset` |
 `linear_product_issue` | `equals`, `in`, `not_in`, `string_contains`, `starts_with`, `is_set`, `is_unset` |
 `shortcut_product_issue` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `product_issue_source` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `product_ticket_completion` | `equals` |
 `number_of_child_issues` | `equals`, `greater_than`, `greater_than_or_equals`, `less_than`, `less_than_or_equals`, `is_set`, `is_unset` |
 `created_in_channel_id` | `equals`, `in`, `not_in`, `string_contains`, `starts_with`, `ends_with`, `is_set`, `is_unset` |
 `product_area` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure, combining conditions, related objects, and operator definitions. The table above lists the operators supported by each issue field.

### Status and issue properties

Standard `state` values:

`new`
`waiting_on_you`
`waiting_on_customer`
`on_hold`
`closed`

Custom status slugs are also supported.

 Field | Values and behavior |
 --- | --- |
 `issue_type` | `conversation` or `ticket`. |
 `is_snoozed` | `true` or `false`. |
 `customer_portal_visible` | `true` or `false`. Issue groups always match `false`. |
 `reopened` | `true` or `false`. Set the first time an issue is reopened after being resolved; stays set and records no timestamp. |
 `parent_issue_group_id` | The ID of the issue group the issue belongs to. |
 `product_area` | A product area slug, such as `billing`. |
 `tags` | A tag name or ID. |

### Messages, timestamps, and counts

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

 Field | Values and behavior |
 --- | --- |
 `subject` | The issue title. `title` is also accepted as a field name. |
 `subject`, `body_html` | `contains` and `does_not_contain` are aliases for `string_contains` and `string_does_not_contain`. |
 `latest_vendor_message_activity_at` | The timestamp of the latest message from your team. |
 `latest_customer_message_activity_at` | The timestamp of the latest message from the customer. |
 `first_message_from`, `last_message_from` | `customer`, `vendor`, or a team ID to match messages from that team's members. For example, `"value": "customer"`. |
 `time_to_first_response` | Seconds by default. Use `"value": "3600"` with `greater_than` for over an hour. `"<N>,seconds"` and `"<N>,milliseconds"` are also accepted. |
 `number_of_touches` | The issue's `number_of_touches` value. |
 `number_of_customer_messages`, `number_of_child_issues` | Whole numbers. |
 `message_redaction_used` | `true` or `false`. |

### Sources, channels, and email

 Field | Values and behavior |
 --- | --- |
 `source` | The issue's source, such as `slack`, `email`, `chat_widget`, or `manual`. Issues created with a `custom_issue_source_id` match that custom source's slug. |
 `slack_channel_id` | The Slack channel ID where the issue was created. |
 `workspace_email` | The email address connected to the Pylon workspace through which the issue's email conversation is routed. |
 `requester_email` | Shorthand for a `related_object` filter on the requester's `email`. |
 `ccs` | The CC addresses on the issue's latest email. |
 `cc_email` | The CC recipients recorded on the issue. |

For `from_email`, `ccs`, and `cc_email`, use an address such as `jane@acme.com`, or `string_contains` with `@acme.com` to match a domain.

`created_in_channel_id` matches the channel where the issue was created. The value depends on the operator:

 Operators | Matches | Example |
 --- | --- | --- |
 `equals`, `in`, `not_in` | Channel ID; for email issues, an email address. | `C0123ABCDEF` or `support@acme.com` |
 `string_contains`, `starts_with`, `ends_with` | Channel name. | `support` |

### Linked engineering tickets

Use the linked ticket's `external_id` from the issue's `external_issues` entry. Each integration uses a different ID format:

 Field | ID format | Example |
 --- | --- | --- |
 `linear_product_issue` | Linear issue UUID. | `2f8c1d3e-6b1a-4c55-9e0f-7a2b3c4d5e6f` |
 `jira_product_issue` | Jira issue numeric ID. | `10042` |
 `github_product_issue` | `owner/repo/number`. | `acme/api/123` |
 `shortcut_product_issue` | Story numeric ID. | `1234` |
 `asana_product_issue` | Task numeric ID. | `1204567890123456` |

Human-readable ticket keys such as `ENG-123`, `PROJ-42`, and `sc-1234` aren't accepted for these filters.

`product_issue_source` accepts:

`asana`
`github`
`jira`
`linear`
`shortcut`

`product_ticket_completion` accepts `any_done` or `all_done`.

### Custom fields

Set `field` to the custom field's slug. If a custom field has the same slug as one of the built-in fields listed above, the custom field is matched instead.

**Rate limit:** 120 requests per minute

`POST /issues/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of issues to fetch. Defaults to 100. Must be between 1 and 1000. |
| `--search-text` | `string` | No | Fuzzy text search. Results are intersected with any provided filter. |
| `--sort` | `object[]` | No | The order of results, as a list of sort keys. Only one sort key is supported right now. Omit for the default order. Send the same sort with every page of a cursor. |

#### `pylon issues snooze`

Snoozes an issue until the specified date and time.

**Rate limit:** 120 requests per minute

`POST /issues/{id}/snooze`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to snooze. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--snooze-until` | `string (date-time)` | Yes | The date and time to snooze the issue until. (RFC3339) |

#### `pylon issues update`

Updates an existing issue. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /issues/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | No | The ID of the account that this issue belongs to. To remove the account, pass an empty string and also provide requester_id. The requester can be cleared with an empty string or retained if it has no account memberships. Account removal is supported only for manual, form, and email issues. |
| `--assignee-id` | `string` | No | The ID of the user who should be assigned to this issue. If empty string is passed in, the issue assignee will be removed. |
| `--custom-fields` | `object[]` | No | An array of custom fields to be used on this issue. Only passed in fields will be modified. |
| `--customer-portal-title` | `string` | No | The customer-facing title displayed in the customer portal, separate from the internal issue title. At most 191 characters. Pass an empty string to clear it. Omit to leave unchanged. |
| `--customer-portal-visible` | `boolean` | No | Whether the issue should be visible in the customer portal. |
| `--requester-id` | `string` | No | The ID of the requester that this issue is on behalf of. If an empty string is passed, the requester will be removed. This field must be provided when removing the issue's account, and a retained requester must not belong to any account. |
| `--requestor-id` | `string` | No | Deprecated: Use requester_id instead. |
| `--state` | `string` | No | The state this issue should be moved to. Standard values are `new`, `waiting_on_you`, `waiting_on_customer`, `on_hold`, and `closed`; custom status slugs are also supported. |
| `--tags` | `string[]` | No | An array of strings to use as tags on this issue, applied according to tags_apply_mode. By default the issue tags will be updated to be exactly the given tags. |
| `--tags-apply-mode` | `append_only \| remove_only \| replace` | No | The mode for applying tags. Valid values: "append_only", "remove_only", "replace". Defaults to "replace". |
| `--team-id` | `string` | No | The ID of the team this issue should be assigned to. If empty string is passed in, any assigned team will be removed. |
| `--title` | `string` | No | The title of the issue. |
| `--type` | `conversation \| ticket` | No | The type of the issue. Set to "ticket" to upgrade a conversation to a support ticket. Cannot be downgraded from "ticket" to "conversation". |

---

### `pylon issues followers`

#### `pylon issues followers add`

By default, adds followers. To remove followers, set the operation field to "remove".

**Rate limit:** 120 requests per minute

`POST /issues/{id}/followers`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to add followers to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--contact-ids` | `string[]` | No | The IDs of contacts to add as followers. |
| `--operation` | `string` | No | Operation to perform. Use "add" to add followers (default) or "remove" to remove followers. |
| `--user-ids` | `string[]` | No | The IDs of users to add as followers. |

#### `pylon issues followers list`

Returns the list of followers for the specified issue.

**Rate limit:** 300 requests per minute

`GET /issues/{id}/followers`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to get followers for. |

---

### `pylon issues messages`

#### `pylon issues messages delete`

Permanently deletes a message from an issue and its connected external system.

**Rate limit:** 30 requests per minute

`DELETE /issues/{id}/messages/{message_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue that the message belongs to. |
| `--message-id` | `string` | Yes | The ID of the message to delete. |

#### `pylon issues messages list`

Returns messages for the specified issue, including replies and internal notes, ordered from oldest to newest.

Set public_only=true to exclude internal notes and hidden messages and remove internal metadata. This option does not authenticate a customer or apply customer-portal access rules.

To post a reply, use the message's top-level id—not thread_id or email_info.message_id. To post an internal note, use an internal thread's thread_id or an internal note's top-level id. Omit both limit and cursor to return all messages; when cursor is provided without limit, the page size defaults to 100.

**Rate limit:** 120 requests per minute

`GET /issues/{id}/messages`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to fetch messages for. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of messages to fetch. Must be greater than 0 and at most 1000. If omitted, all messages are returned for backward compatibility. |
| `--public-only` | `boolean` | No | Return only customer-visible messages, excluding internal notes and hidden messages. Clears BCC recipients, email-open tracking, Slack metadata, internal thread IDs, and the author's internal user email. Defaults to false. This does not enforce a portal visitor's ticket access or portal identity settings; callers must authorize their customers separately. |

#### `pylon issues messages redact`

Permanently replaces a message's stored content with redacted_body_message and optionally deletes its attachments. This action cannot be undone.
When omitted, redacted_body_message defaults to "This message has been redacted." and redact_attachments defaults to true.

**Rate limit:** 120 requests per minute

`POST /issues/{id}/messages/{message_id}/redact`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue that the message belongs to. |
| `--message-id` | `string` | Yes | The ID of the message to redact. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--redact-attachments` | `boolean` | No | Whether to permanently delete the message's attachments. Defaults to true. |
| `--redacted-body-message` | `string` | No | Replacement message body in HTML. The caller is responsible for replacing any sensitive portions. Defaults to "This message has been redacted." |

#### `pylon issues messages update`

Replaces the body of a message and syncs the edit to its connected channel (Slack, Microsoft Teams, Discord, Google Chat, Telegram, or the chat widget).
Only messages authored by the API token's user can be edited. Emails, customer messages, and redacted messages cannot be edited.
Callers without issue write access can edit only their own internal notes.

**Rate limit:** 30 requests per minute

`PATCH /issues/{id}/messages/{message_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue that the message belongs to. |
| `--message-id` | `string` | Yes | The ID of the message to edit. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--body-html` | `string` | Yes | The new message body in HTML. Replaces the existing body. |

---

### `pylon issues survey-responses`

#### `pylon issues survey-responses list`

Returns paginated CSAT and custom survey responses associated with an issue.

**Rate limit:** 300 requests per minute

`GET /issues/{id}/survey-responses`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue. |
| `--survey-id` | `string` | No | Filter responses by survey template ID. |
| `--submitted-after` | `string (date-time)` | No | Filter responses submitted after this time (RFC3339 format). |
| `--submitted-before` | `string (date-time)` | No | Filter responses submitted before this time (RFC3339 format). |
| `--cursor` | `string` | No | The cursor for pagination. |
| `--limit` | `integer (int64)` | No | The number of responses to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

---

### `pylon issues threads`

#### `pylon issues threads create`

Creates a new internal thread on an issue.

**Rate limit:** 120 requests per minute

`POST /issues/{id}/threads`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to create a thread for. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--name` | `string` | No | The name of the thread. |
| `--slack-channel-id` | `string` | No | The Slack channel ID to sync the thread to. When slack_thread_ts is also provided, links that existing Slack thread. Otherwise, creates a new Slack-backed thread. Linking an existing Slack thread imports its message history and enables ongoing synchronization. Creating or linking a Slack-backed thread requires an API token configured to act as a human Pylon user whose verified Slack identity is a member of the channel. Pylon bot users and standalone API identities are not supported because they do not have Slack-verifiable channel membership. |
| `--slack-thread-ts` | `string` | No | The root message timestamp of an existing Slack thread to link. Requires slack_channel_id. |

#### `pylon issues threads list`

Returns all threads for the specified issue.

**Rate limit:** 120 requests per minute

`GET /issues/{id}/threads`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to fetch threads for. |

---

### `pylon issues voice-calls`

#### `pylon issues voice-calls list`

Returns voice call records for the specified phone issue. Each call includes its participants and its recordings, with parsed transcript segments and a presigned download URL for the audio file. Recordings whose transcript has not yet completed are omitted; refetch later to see them.

**Rate limit:** 120 requests per minute

`GET /issues/{id}/voice-calls`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to fetch voice calls for. |

---

### `pylon knowledge-bases`

#### `pylon knowledge-bases get`

Returns a single knowledge base by ID.

**Rate limit:** 300 requests per minute

`GET /knowledge-bases/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base. |

#### `pylon knowledge-bases list`

Returns all knowledge bases for the organization.

**Rate limit:** 300 requests per minute

`GET /knowledge-bases`

---

### `pylon knowledge-bases articles`

#### `pylon knowledge-bases articles create`

Creates a new article within a knowledge base.

**Rate limit:** 30 requests per minute

`POST /knowledge-bases/{id}/articles`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the article is being added to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--author-user-id` | `string` | Yes | The ID of the user attributed as the author of the article. |
| `--body-html` | `string` | No | The HTML body of the article. Required unless body_markdown is set. |
| `--body-markdown` | `string` | No | The body of the article in markdown, instead of body_html. |
| `--collection-id` | `string` | No | The ID of the collection containing the article. |
| `--is-published` | `boolean` | No | Whether the article should be published. Defaults to false. |
| `--is-unlisted` | `boolean` | No | Whether the article is accessible only via a direct link. Defaults to false. |
| `--position` | `integer (int64)` | No | The zero-based position among the parent's articles and subcollections. Defaults to the end. Positions beyond the end append the article. |
| `--slug` | `string` | No | The slug of the article. Defaults to a slug based on the title. |
| `--title` | `string` | Yes | The title of the article. |
| `--translations` | `object[]` | No | Translations of the article content in different languages |
| `--visibility-config` | `object` | No |  |

#### `pylon knowledge-bases articles delete`

Permanently deletes an article from the knowledge base.

**Rate limit:** 120 requests per minute

`DELETE /knowledge-bases/{id}/articles/{article_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The KnowledgeBaseID of the article to delete. |
| `--article-id` | `string` | Yes | The ID of the article to delete. |

#### `pylon knowledge-bases articles get`

Returns a single article by ID within the specified knowledge base.

**Rate limit:** 300 requests per minute

`GET /knowledge-bases/{id}/articles/{article_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The KnowledgeBaseID of the article to fetch. |
| `--article-id` | `string` | Yes | The ID of the article to fetch. |
| `--language` | `string` | No | The language code to fetch the article in. If not provided, returns the default language. |

#### `pylon knowledge-bases articles list`

Returns a paginated list of articles for the specified knowledge base.

**Rate limit:** 120 requests per minute

`GET /knowledge-bases/{id}/articles`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the articles are being fetched from. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of articles to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |
| `--language` | `string` | No | The language code to fetch articles in. If not provided, returns the default language. |
| `--media` | `all \| none` | No | Controls whether embedded media is included in article HTML. Valid values are all (default) and none. When set to none, embedded images, video, audio, and inline media are removed while descriptive text and standard links are preserved. |

#### `pylon knowledge-bases articles request-review`

Requests human and/or AI review on the article's current draft version. At least one of `reviewer_user_ids` or `request_ai_review` must be provided. The article must have an unpublished current version. Requesting AI review requires the organization to have AI article review enabled.

**Rate limit:** 30 requests per minute

`POST /knowledge-bases/{id}/articles/{article_id}/request-review`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the article belongs to. |
| `--article-id` | `string` | Yes | The ID of the article to request review for. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--request-ai-review` | `boolean` | No | When true, also queue an AI review. Requires the organization to have AI article review enabled. |
| `--reviewer-user-ids` | `string[]` | No | IDs of users to request a human review from. Each user must already be a configured reviewer for the article's knowledge base. |

#### `pylon knowledge-bases articles update`

Updates an existing article. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /knowledge-bases/{id}/articles/{article_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The KnowledgeBaseID of the article to update. |
| `--article-id` | `string` | Yes | The ID of the article to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--author-user-id` | `string` | No | The ID of the user in this organization attributed as the author of the article. Does not change version authorship. |
| `--body-html` | `string` | No | The HTML body of the article. Saved as a new draft; the published article changes only if publish_updated_body_html or is_published is true. |
| `--body-markdown` | `string` | No | The body of the article in markdown, instead of body_html. Saved and published the same way. |
| `--collection-id` | `string` | No | The ID of the collection containing the article. |
| `--is-published` | `boolean` | No | Whether the article should be published or unpublished. |
| `--is-unlisted` | `boolean` | No | Whether the article is accessible only via a direct link. |
| `--language` | `string` | No | The language code of the translation to update. If not provided, the default language (original article) will be updated. |
| `--position` | `integer (int64)` | No | The zero-based position among the parent's articles and subcollections. Omit to keep the current position, or append when moving to another collection. Positions beyond the end append the article. When collection_id is provided, applies within the destination collection. |
| `--publish-updated-body-html` | `boolean` | No | Whether to publish the updated body_html. Defaults to false, which leaves the change as a draft. |
| `--tag-ids` | `string[]` | No | IDs of article tags to assign, applied according to tags_apply_mode. By default replaces all tags currently assigned to the article. |
| `--tags-apply-mode` | `append_only \| remove_only \| replace` | No | The mode for applying tag_ids. Valid values: "append_only", "remove_only", "replace". Defaults to "replace". |
| `--title` | `string` | No | The title of the article. For the default language, applies to the live article immediately. |
| `--visibility-config` | `object` | No |  |

---

### `pylon knowledge-bases collections`

#### `pylon knowledge-bases collections create`

Creates a new collection within a knowledge base.

**Rate limit:** 30 requests per minute

`POST /knowledge-bases/{id}/collections`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the article is being added to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--description` | `string` | No | Description of the collection. |
| `--parent-collection-id` | `string` | No | The ID of the parent collection. |
| `--slug` | `string` | No | The slug of the collection. Defaults to a slug based on the title. |
| `--title` | `string` | Yes | The title of the collection. |
| `--visibility-config` | `object` | No |  |

#### `pylon knowledge-bases collections delete`

Permanently deletes a collection and all articles within it from the knowledge base. Nested collections and their articles are also deleted.

**Rate limit:** 30 requests per minute

`DELETE /knowledge-bases/{id}/collections/{collection_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base that the collection belongs to. |
| `--collection-id` | `string` | Yes | The ID of the collection to delete. |

#### `pylon knowledge-bases collections get`

Returns a single collection by ID within the specified knowledge base.

**Rate limit:** 120 requests per minute

`GET /knowledge-bases/{id}/collections/{collection_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base |
| `--collection-id` | `string` | Yes | The ID of the collection |

#### `pylon knowledge-bases collections list`

Returns all collections for the specified knowledge base.

**Rate limit:** 120 requests per minute

`GET /knowledge-bases/{id}/collections`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base |

#### `pylon knowledge-bases collections update`

Updates an existing collection. Only provided fields are modified.

**Rate limit:** 30 requests per minute

`PATCH /knowledge-bases/{id}/collections/{collection_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base that the collection belongs to. |
| `--collection-id` | `string` | Yes | The ID of the collection to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--description` | `string` | No | The description of the collection. |
| `--slug` | `string` | No | The slug of the collection. |
| `--title` | `string` | No | The title of the collection. |
| `--visibility-config` | `object` | No |  |

---

### `pylon knowledge-bases route-redirects`

#### `pylon knowledge-bases route-redirects create`

Creates a path redirect within a knowledge base, mapping a source path to an article or collection.

**Rate limit:** 30 requests per minute

`POST /knowledge-bases/{id}/route-redirects`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the route redirect is being added to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--from-path` | `string` | Yes | The path to redirect from. |
| `--language` | `string` | No | Language of the object to redirect to. If not specified, the default language of the knowledge base will be used. |
| `--object-id` | `string` | No | The ID of the article or collection to redirect to. Omit when object_type is "knowledgebase". |
| `--object-type` | `string` | Yes | The type of the object to redirect to: "article", "collection", or "knowledgebase" for the knowledge base homepage. |

#### `pylon knowledge-bases route-redirects delete`

Deletes a path redirect from a knowledge base. Requires knowledge base admin permission.

**Rate limit:** 30 requests per minute

`DELETE /knowledge-bases/{id}/route-redirects/{redirect_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base. |
| `--redirect-id` | `string` | Yes | The ID of the route redirect. |

#### `pylon knowledge-bases route-redirects list`

Returns every path redirect in a knowledge base.

**Rate limit:** 300 requests per minute

`GET /knowledge-bases/{id}/route-redirects`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base. |

---

### `pylon knowledge-bases themes`

#### `pylon knowledge-bases themes get`

Returns a theme's editable files, including current draft and published content.

**Rate limit:** 300 requests per minute

`GET /knowledge-bases/{id}/themes/{theme_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base. |
| `--theme-id` | `string` | Yes | The ID of the theme. |

#### `pylon knowledge-bases themes publish`

Promotes all current draft files to their published versions. Changes become live immediately when this is the knowledge base's active theme. Publishing a theme with no draft changes is a no-op.

**Rate limit:** 120 requests per minute

`POST /knowledge-bases/{id}/themes/{theme_id}/publish`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base. |
| `--theme-id` | `string` | Yes | The ID of the theme. |

#### `pylon knowledge-bases themes update`

Replaces one or more complete theme files in a single atomic draft update. Use the publish endpoint to make the changes live.

**Rate limit:** 120 requests per minute

`PATCH /knowledge-bases/{id}/themes/{theme_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base. |
| `--theme-id` | `string` | Yes | The ID of the theme. |

Required request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--assets` | `object[]` | Yes | The complete theme files to replace. Changes are saved as drafts and are not published. |

---

### `pylon macro-groups`

#### `pylon macro-groups list`

Returns all macro groups for the organization.

**Rate limit:** 300 requests per minute

`GET /macro-groups`

---

### `pylon macros`

#### `pylon macros create`

Creates a new macro within the specified macro group.

**Rate limit:** 300 requests per minute

`POST /macros`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--conditions` | `object` | No |  |
| `--edit-visibility` | `object` | No |  |
| `--macro-group-id` | `string` | Yes | The ID of the macro group this macro belongs to. |
| `--name` | `string` | Yes | The name of the macro. |
| `--text-html` | `string` | Yes | The HTML content of the macro. |
| `--text-type` | `string` | No | The type of text: "reply", "note", or "email". Defaults to "reply". |
| `--visibility` | `object` | No |  |

#### `pylon macros delete`

Permanently deletes a macro by ID.

**Rate limit:** 120 requests per minute

`DELETE /macros/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the macro to delete. |

#### `pylon macros get`

Returns a single macro by ID.

**Rate limit:** 300 requests per minute

`GET /macros/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the macro. |

#### `pylon macros list`

Returns all macros for the organization. Optionally filter by macro group ID.

**Rate limit:** 300 requests per minute

`GET /macros`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--macro-group-id` | `string` | No | Filter macros by macro group ID. |

#### `pylon macros update`

Updates an existing macro by ID. All fields are optional; only provided fields will be updated.

**Rate limit:** 300 requests per minute

`PATCH /macros/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the macro to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--conditions` | `object` | No |  |
| `--edit-visibility` | `object` | No |  |
| `--macro-group-id` | `string` | No | The ID of the macro group this macro belongs to. |
| `--name` | `string` | No | The name of the macro. |
| `--text-html` | `string` | No | The HTML content of the macro. |
| `--text-type` | `string` | No | The type of text: "reply", "note", or "email". |
| `--visibility` | `object` | No |  |

---

### `pylon me`

#### `pylon me get`

Returns the organization and user associated with the credentials used for authentication.

**Rate limit:** 300 requests per minute

`GET /me`

---

### `pylon milestones`

#### `pylon milestones create`

Creates a new milestone within a project.

**Rate limit:** 300 requests per minute

`POST /milestones`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | No | Account ID for this project |
| `--due-date` | `string (date-time)` | No | Due date for this milestone, in RFC 3339 format |
| `--name` | `string` | Yes | Name for this milestone |
| `--project-id` | `string` | Yes | Project ID for this milestone |

#### `pylon milestones delete`

Permanently deletes a milestone by ID.

**Rate limit:** 300 requests per minute

`DELETE /milestones/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the milestone to delete. |

#### `pylon milestones get`

Returns a single milestone by ID.

**Rate limit:** 300 requests per minute

`GET /milestones/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the milestone to fetch. |

#### `pylon milestones search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `project_id` | `equals`, `in`, `not_in` |
 `account_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `due_date` | `time_is_after`, `time_is_before`, `time_range`, `is_set`, `is_unset` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |
 `started_at` | `time_is_after`, `time_is_before`, `time_range`, `is_set` |
 `completed_at` | `time_is_after`, `time_is_before`, `time_range`, `is_set` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Timestamp values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

### Project availability

Milestones belonging to an unlaunched project are not returned.

**Rate limit:** 120 requests per minute

`POST /milestones/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of milestones to fetch. Defaults to 100. Must be between 1 and 1000. |

#### `pylon milestones update`

Updates an existing milestone. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /milestones/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the milestone to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--due-date` | `string` | No | Due date for this milestone, in RFC 3339 format. Set to an empty string to clear it. |
| `--name` | `string` | No | Name for this milestone |

---

### `pylon projects`

#### `pylon projects create`

Creates a new project for an account. Provide a name or project_template_id. A template supplies defaults; non-empty name and description_html values and supplied ai_instructions, customer_portal_visible, and owner_id values override them. Supplying either start_date or end_date replaces both template dates.

**Rate limit:** 300 requests per minute

`POST /projects`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | Yes | Account ID for this project |
| `--ai-instructions` | `string` | No | Instructions the AI follows when keeping this smart project up to date. Overrides the template's instructions when provided. |
| `--customer-portal-visible` | `boolean` | No | Customer portal visible for this project |
| `--description-html` | `string` | No | Description HTML for this project |
| `--end-date` | `string (date-time)` | No | End date for this project, in RFC 3339 format |
| `--name` | `string` | No | Name for this project. Required unless project_template_id is provided. When both are provided, this name overrides the template's name. |
| `--owner-id` | `string` | No | Owner ID for this project |
| `--project-template-id` | `string` | No | Project template ID for this project. When provided, it supplies defaults; non-empty name and description_html values and supplied ai_instructions, customer_portal_visible, and owner_id values override them. Supplying either start_date or end_date replaces both template dates. |
| `--start-date` | `string (date-time)` | No | Start date for this project, in RFC 3339 format |

#### `pylon projects delete`

Permanently deletes a project by ID.

**Rate limit:** 120 requests per minute

`DELETE /projects/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the project to delete. |

#### `pylon projects get`

Returns a single project by ID.

**Rate limit:** 300 requests per minute

`GET /projects/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the project to fetch. |

#### `pylon projects search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `account_id` | `equals`, `in`, `not_in`, `is_set` |
 `status` | `equals`, `in`, `not_in` |
 `owner_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `is_archived` | `equals` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Filter values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

`status` accepts:

`not_started`
`in_progress`
`completed`

### Custom fields

Set `field` to the custom field's slug.

**Rate limit:** 120 requests per minute

`POST /projects/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of projects to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

#### `pylon projects update`

Updates an existing project. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /projects/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the project to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--ai-instructions` | `string` | No | Instructions the AI follows when keeping this smart project up to date. Set to an empty string to clear them. |
| `--custom-fields` | `object[]` | No | An array of custom fields to be used on this project. Only passed in fields will be modified. |
| `--customer-portal-visible` | `boolean` | No | Customer portal visible for this project |
| `--description-html` | `string` | No | Description HTML for this project |
| `--end-date` | `string` | No | End date for this project, in RFC 3339 format. Set to an empty string to clear it. |
| `--is-archived` | `boolean` | No | Whether the project is archived |
| `--name` | `string` | No | Name for this project |
| `--owner-id` | `string` | No | Owner ID for this project |
| `--start-date` | `string` | No | Start date for this project, in RFC 3339 format. Set to an empty string to clear it. |

---

### `pylon surveys`

#### `pylon surveys get`

Returns a single survey by ID.

**Rate limit:** 300 requests per minute

`GET /surveys/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the survey. |

#### `pylon surveys list`

Returns all surveys for the organization.

**Rate limit:** 300 requests per minute

`GET /surveys`

#### `pylon surveys search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Timestamp values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

**Rate limit:** 120 requests per minute

`POST /surveys/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of surveys to fetch. Defaults to 100. Must be between 1 and 1000. |

---

### `pylon surveys responses`

#### `pylon surveys responses list`

Returns paginated survey responses visible to the caller, optionally filtered by time range, account, or contact.

**Rate limit:** 300 requests per minute

`GET /surveys/{id}/responses`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the survey. |
| `--submitted-after` | `string (date-time)` | No | Filter responses submitted after this time (RFC3339 format). |
| `--submitted-before` | `string (date-time)` | No | Filter responses submitted before this time (RFC3339 format). |
| `--account-id` | `string` | No | Filter responses by account ID. Required with contact_id when the caller has scoped account or contact access. |
| `--contact-id` | `string` | No | Filter responses by contact ID. Required with account_id when the caller has scoped account or contact access. |
| `--cursor` | `string` | No | The cursor for pagination. |
| `--limit` | `integer (int64)` | No | The number of responses to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

---

### `pylon tags`

#### `pylon tags create`

Creates a new tag with the specified value and object type.

**Rate limit:** 300 requests per minute

`POST /tags`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--hex-color` | `string` | No | The hex code of the tag's color. |
| `--object-type` | `account \| article \| issue` | Yes | The object type of the associated object. Can be "account", "article", or "issue". |
| `--value` | `string` | Yes | The tag value. |

#### `pylon tags delete`

Permanently deletes a tag by ID.

**Rate limit:** 30 requests per minute

`DELETE /tags/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the tag to update. |

#### `pylon tags get`

Returns a single tag by ID.

**Rate limit:** 300 requests per minute

`GET /tags/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the tag. |

#### `pylon tags list`

Returns all tags for the organization.

**Rate limit:** 300 requests per minute

`GET /tags`

#### `pylon tags search`

Returns tags the caller can read, newest first, optionally narrowed to one object type and to values containing search_text.

**Rate limit:** 120 requests per minute

`POST /tags/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of tags to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |
| `--object-type` | `account \| article \| issue` | No | Only return tags of this object type. Omit to search every type the caller can read. |
| `--search-text` | `string` | No | Only return tags whose value contains this text. Spaces, hyphens, and underscores match each other. |

#### `pylon tags update`

Updates an existing tag. Only provided fields are modified.

**Rate limit:** 30 requests per minute

`PATCH /tags/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the tag to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--hex-color` | `string` | No | The hex code of the tag's color. |
| `--value` | `string` | No | in: body The name of the tag. |

---

### `pylon task-statuses`

#### `pylon task-statuses list`

Returns all task statuses for the organization.

**Rate limit:** 30 requests per minute

`GET /task-statuses`

---

### `pylon tasks`

#### `pylon tasks create`

Creates a new task with a title and optional metadata.

**Rate limit:** 300 requests per minute

`POST /tasks`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--account-id` | `string` | No | Account ID for this task |
| `--ai-instructions` | `string` | No | Instructions the AI follows when evaluating this task in a smart project |
| `--assignee-id` | `string` | No | Assignee ID for this task |
| `--blocked-by-task-ids` | `string[]` | No | IDs of existing tasks that block this task |
| `--body-html` | `string` | No | Body HTML for this task |
| `--custom-fields` | `object[]` | No | An array of custom fields to be used on this task. |
| `--customer-portal-visible` | `boolean` | No | Customer portal visible for this task |
| `--due-date` | `string (date-time)` | No | Due date for this task, in RFC 3339 format |
| `--milestone-id` | `string` | No | Milestone ID for this task |
| `--parent-task-id` | `string` | No | Parent task ID, to create this task as a subtask |
| `--project-id` | `string` | No | Project ID for this task |
| `--status` | `string` | No |  |
| `--title` | `string` | Yes | Title for this task |

#### `pylon tasks delete`

Permanently deletes a task by ID.

**Rate limit:** 120 requests per minute

`DELETE /tasks/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to delete. |

#### `pylon tasks get`

Returns a single task by ID.

**Rate limit:** 300 requests per minute

`GET /tasks/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to fetch. |

#### `pylon tasks link-external-issue`

By default, links the external issue. To unlink it, set the operation field to "unlink". Repeating the same link request is a successful no-op.

**Rate limit:** 120 requests per minute

`POST /tasks/{id}/external-issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to link an external issue to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--external-issue-id` | `string` | Yes | The ID or human-readable key of the external issue in the source system. |
| `--operation` | `string` | No | Operation to perform. Use "link" to link the issue (default) or "unlink" to unlink it. |
| `--source` | `string` | Yes | The source system of the external issue (e.g., "linear", "asana", "jira", "github", "shortcut"). |

#### `pylon tasks link-issue`

Links the issue to the task by default. To unlink it, set the operation field to "unlink".

**Rate limit:** 120 requests per minute

`POST /tasks/{id}/issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to link a Pylon issue to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--issue-id` | `string` | Yes | The ID of the Pylon issue. |
| `--operation` | `string` | No | Operation to perform. Use "link" to link the issue (default) or "unlink" to unlink it. |

#### `pylon tasks list`

Returns a paginated list of tasks for the organization.

**Rate limit:** 300 requests per minute

`GET /tasks`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of tasks to fetch. Defaults to 100. Must be greater than 0 and less than 1000. |

#### `pylon tasks search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `account_id` | `equals`, `in`, `not_in`, `is_set` |
 `project_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `status` | `equals`, `in`, `not_in` |
 `assignee_id` | `equals`, `in`, `not_in`, `is_set` |
 `milestone_id` | `equals`, `in`, `not_in`, `is_set` |
 `created_at` | `time_is_after`, `time_is_before`, `time_range` |
 `due_date` | `time_is_after`, `time_is_before`, `time_range`, `is_set` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

### Filter values

Timestamp values use RFC 3339 format, such as `2026-10-01T00:00:00Z`.

`status` accepts:

`not_started`
`in_progress`
`completed`

### Custom fields

Set `field` to the custom field's slug.

**Rate limit:** 120 requests per minute

`POST /tasks/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of tasks to fetch. Defaults to 100. Must be between 1 and 1000. |

#### `pylon tasks update`

Updates an existing task. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /tasks/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--ai-instructions` | `string` | No | Instructions the AI follows when evaluating this task in a smart project. Set to an empty string to clear them. |
| `--assignee-id` | `string` | No | Assignee ID for this task |
| `--blocked-by-task-ids` | `string[]` | No | IDs of the tasks that block this task. If provided, replaces the task's current blocking tasks; pass an empty array to remove them all. |
| `--body-html` | `string` | No | Body HTML for this task |
| `--completed-at` | `string (date-time)` | No | Completed at time for this task, in RFC 3339 format. The task must already have a completed status and completion date. |
| `--custom-fields` | `object[]` | No | An array of custom fields to be used on this task. Only passed in fields will be modified. |
| `--customer-portal-visible` | `boolean` | No | Customer portal visible for this task |
| `--due-date` | `string` | No | Due date for this task, in RFC 3339 format. Set to an empty string to clear it. |
| `--milestone-id` | `string` | No | Milestone ID for this task |
| `--project-id` | `string` | No | Project ID for this task |
| `--status` | `string` | No |  |
| `--title` | `string` | No | Title for this task |

---

### `pylon tasks comments`

#### `pylon tasks comments create`

Creates a new comment on a task. The authenticated user is the author.

**Rate limit:** 120 requests per minute

`POST /tasks/{id}/comments`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to add a comment to. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--body-html` | `string` | Yes | The body of the comment in HTML format. |
| `--is-internal` | `boolean` | No | Whether the comment is visible only to internal users. |

#### `pylon tasks comments delete`

Deletes an existing comment. Only the original author can delete their comment.

**Rate limit:** 120 requests per minute

`DELETE /tasks/{id}/comments/{comment_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task. |
| `--comment-id` | `string` | Yes | The ID of the comment to delete. |

#### `pylon tasks comments list`

Returns all comments for a task, ordered by creation time.

**Rate limit:** 300 requests per minute

`GET /tasks/{id}/comments`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to fetch comments for. |

#### `pylon tasks comments update`

Updates an existing comment. Only the original author can update their comment.

**Rate limit:** 120 requests per minute

`PATCH /tasks/{id}/comments/{comment_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task. |
| `--comment-id` | `string` | Yes | The ID of the comment to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--body-html` | `string` | Yes | The updated body of the comment in HTML format. |

---

### `pylon teams`

#### `pylon teams create`

Creates a new team with a name and optional member list. Optionally sets how the team
assigns issues and creates its recurring assignment schedule in the same call.

**Rate limit:** 30 requests per minute

`POST /teams`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--assignment-configuration` | `object` | No |  |
| `--name` | `string` | Yes | The name of the team. |
| `--schedule` | `object` | No |  |
| `--user-ids` | `string[]` | No | The list of user IDs to add to the team. |

#### `pylon teams delete`

Delete an existing team
Deletes a team and its memberships and schedules. Subteams are detached and remain available.
Teams referenced by other configuration or owning internal accounts cannot be deleted until those references are removed.

**Rate limit:** 30 requests per minute

`DELETE /teams/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the team to delete. |

#### `pylon teams get`

Returns a single team by ID, with how it assigns issues and its recurring assignment
schedule if it has one.

**Rate limit:** 300 requests per minute

`GET /teams/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the team to fetch. |

#### `pylon teams list`

Returns all teams for the organization, each with how it assigns issues and its recurring
assignment schedule if it has one.

**Rate limit:** 300 requests per minute

`GET /teams`

#### `pylon teams update`

Updates an existing team, including how it assigns issues and its recurring assignment
schedule. Only provided fields are modified; supplying schedule.blocks replaces the whole
rotation, and omitting it leaves the rotation unchanged.

**Rate limit:** 120 requests per minute

`PATCH /teams/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the team to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--assignment-configuration` | `object` | No |  |
| `--name` | `string` | No | The name of the team. |
| `--schedule` | `object` | No |  |
| `--user-ids` | `string[]` | No | The list of user IDs to add to the team. If provided, the team members will be updated to be exactly the given users. |

---

### `pylon ticket-forms`

#### `pylon ticket-forms get`

Returns a single ticket form by ID.

**Rate limit:** 300 requests per minute

`GET /ticket-forms/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the ticket form to fetch. |

#### `pylon ticket-forms list`

Returns all ticket forms for the organization.

**Rate limit:** 300 requests per minute

`GET /ticket-forms`

#### `pylon ticket-forms submit`

Creates an issue from a configured ticket form. Provide either requester_id or both requester_email and requester_name. Field types are inferred from the ticket form; use value for single-value fields and values for multi-value and file-upload fields.

**Rate limit:** 30 requests per minute

`POST /ticket-forms/{id}/submissions`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the ticket form to submit. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--attachment-urls` | `string[]` | No | HTTPS URLs to attach to the initial ticket message. URLs are copied into durable Pylon storage before the submission is persisted. |
| `--fields` | `object[]` | No | The submitted ticket form fields. Use the slugs returned by GET /ticket-forms/{id}, excluding name and email, which are supplied through the requester fields above. |
| `--requester-email` | `string` | No | The requester's email address. Must be provided with requester_name and cannot be combined with requester_id. |
| `--requester-id` | `string` | No | The ID of an existing contact to use as the requester. Provide either requester_id or both requester_email and requester_name. |
| `--requester-name` | `string` | No | The requester's full name. Must be provided with requester_email and cannot be combined with requester_id. |

---

### `pylon training-data`

#### `pylon training-data create`

Creates a new training data configuration for the organization.

**Rate limit:** 30 requests per minute

`POST /training-data`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--training-data-name` | `string` | No | The name of the training data container. |
| `--visibility` | `everyone \| user_only \| ai_agent_only` | No | The visibility of the training data. Defaults to "everyone". Valid values: "everyone", "user_only", "ai_agent_only" |

#### `pylon training-data get`

Returns a single training data configuration by ID.

**Rate limit:** 300 requests per minute

`GET /training-data/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the training data. |

#### `pylon training-data list`

Returns all training data configurations for the organization.

**Rate limit:** 300 requests per minute

`GET /training-data`

#### `pylon training-data upload-content`

Uploads plain text content as a training data document.

**Rate limit:** 30 requests per minute

`POST /training-data/upload-content`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--content` | `string` | No | The text content to upload. |
| `--external-id` | `string` | No | External ID for idempotent operations (optional). |
| `--file-name` | `string` | No | The name for the uploaded file. |
| `--training-data-id` | `string` | No | The ID of an existing training data container to upload to (optional). |
| `--training-data-name` | `string` | No | The name of a new training data container (required if training_data_id not provided). |
| `--visibility` | `everyone \| user_only \| ai_agent_only` | No | Visibility of the training data. Defaults to "everyone". |

#### `pylon training-data upload-files`

Uploads one or more files to a training data configuration.

**Rate limit:** 30 requests per minute

`POST /training-data/upload`

Optional multipart request body: supply the form-field flags below; binary fields accept local file paths.

Top-level multipart fields are listed below. Required indicates a required form field.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--external-ids` | `string[]` | No | External IDs for idempotent operations. Must match the number of files if provided. Used for duplicate detection and updates. |
| `--file-names` | `string[]` | No | Custom names for the uploaded files. Must match the number of files if provided. If not provided, original filenames will be used. |
| `--files` | `string[]` | Yes | The files to upload (minimum 1, maximum 10). Supported types: PDF, plain text, markdown, CSV, JSON, and images (JPEG, PNG, GIF, WebP). Maximum size: 50MB per file, 100MB total. |
| `--training-data-id` | `string` | No | The ID of an existing training data container to upload files to. Required if not creating new training data. |
| `--training-data-name` | `string` | No | The name of a new training data container. Required when creating new training data (if training_data_id is not provided). |
| `--visibility` | `everyone \| user_only \| ai_agent_only` | No | Visibility of the training data. Defaults to "everyone". Valid values: "everyone", "user_only", "ai_agent_only" |

---

### `pylon training-data documents`

#### `pylon training-data documents delete`

Removes documents from a training data configuration by document ID or external ID.

**Rate limit:** 30 requests per minute

`DELETE /training-data/{id}/documents`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the training data. |
| `--document-ids` | `string[]` | No | Document IDs to delete. |
| `--external-ids` | `string[]` | No | External IDs to delete. |

---

### `pylon user-roles`

#### `pylon user-roles list`

Returns all user roles for the organization, with the actions each role grants.
Permission and issue access rule filters use the same filter shape that search endpoints accept;
a filter the API can't represent is omitted and marked filter_unsupported. A "current_user"
value in a filter means the user the permission is checked for.

**Rate limit:** 300 requests per minute

`GET /user-roles`

---

### `pylon user-statuses`

#### `pylon user-statuses list`

Returns the built-in and custom user statuses for the organization. Use `slug` in a team's `assignment_configuration.assignable_user_statuses`.

**Rate limit:** 30 requests per minute

`GET /user-statuses`

---

### `pylon users`

#### `pylon users get`

Returns a single user by ID.

**Rate limit:** 300 requests per minute

`GET /users/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the user to fetch. |

#### `pylon users invite`

Creates a user and emails them an invitation to join the organization. If a user with this email already exists,
they are reactivated if needed and sent a new invitation, and any pending invitation is canceled. Requires admin permissions.

**Rate limit:** 30 requests per minute

`POST /users/invite`

Required request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--email` | `string` | Yes | The email address to send the invitation to. |
| `--name` | `string` | Yes | The name of the user to invite. |
| `--role-id` | `string` | No | The ID of the role to give the user. See GET /user-roles. Defaults to the organization's default role. |

#### `pylon users list`

Returns all users for the organization.

**Rate limit:** 300 requests per minute

`GET /users`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--include-deactivated` | `boolean` | No | Whether to include deactivated users. Defaults to false. |

#### `pylon users search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `email` | `equals`, `in`, `not_in` |

### Filter syntax and operators

See [Search filters](https://docs.usepylon.com/pylon-docs/developer/api/conventions#search-filters) for filter structure and operator definitions. The table above lists the operators supported by each field.

**Rate limit:** 120 requests per minute

`POST /users/search`

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--filter` | `object` | No |  |
| `--limit` | `integer (int64)` | No | The number of users to fetch. Defaults to 100. Must be between 1 and 1000. |

#### `pylon users update`

Updates an existing user. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /users/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the user to update. |

Optional request body: supply `--json <JSON|->` or individual body-field flags.

Top-level body-field flags are listed below. Required indicates a required property in the body, which can also be supplied through `--json`.

| Flag | Type | Required in body | Description |
|------|------|------------------|-------------|
| `--avatar-url` | `string` | No | The avatar URL of the user. Must be a square .png, .jpg or .jpeg. |
| `--is-deactivated` | `boolean` | No | Whether the user is deactivated. Changing it requires admin permissions. Deactivating revokes the user's API tokens, removes their team schedules and skills, disconnects their calendars, and reassigns their open issues in the background. Reactivating does not restore any of these. Users provisioned through SCIM must be deactivated and reactivated in the identity provider. |
| `--name` | `string` | No | The name of the user. |
| `--reassign-open-issues-to-user-id` | `string` | No | The ID of the user to reassign the deactivated user's open issues to. Only valid with `is_deactivated: true`. If omitted, the issues are unassigned. |
| `--role-id` | `string` | No | The role_id of the user. |
| `--status` | `string` | No | The new status for the user: `active`, `away`, `out_of_office`, or a custom status slug from GET /user-statuses. |

---

## Global flags

These flags are available on every command:

| Flag | Description |
|------|-------------|
| `--dry-run` | Print the HTTP request without sending it |
| `--json <JSON\|->` | Supply the request body as JSON (or `-` for stdin) |
| `--params <JSON>` | Merge extra parameters as JSON |
| `--format <json\|table\|yaml\|csv>` | Output format (default: `json`) |
| `--output <PATH>` | Write binary responses to a file |
| `--base-url <URL>` | Override the API base URL |
| `--no-extract` | Print the full response body instead of the `x-fern-sdk-return-value` extraction |
| `--no-retry` | Disable retries declared by `x-fern-retries`, including network errors |
| `-q, --quiet` | Suppress stdout on success |
| `-h, --help` | Print help |
| `-V, --version` | Print version |

Operations the spec describes how to page (via `x-fern-pagination` or a root `page_token` parameter) also accept:

| Flag | Description |
|------|-------------|
| `--page-all` | Auto-paginate and stream all results |
| `--page-limit <N>` | Max pages to fetch (default: `10`) |
| `--page-delay <MS>` | Delay between page fetches in milliseconds (default: `100`) |
| `--no-pager` | Disable the pager even on interactive terminals |

Operations the spec marks as streaming (via `x-fern-streaming`) also accept:

| Flag | Description |
|------|-------------|
| `--no-stream` | Buffer the streaming response and print it as a single value once complete |

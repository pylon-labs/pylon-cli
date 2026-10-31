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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon accounts create`

Creates a new account with the specified name and optional metadata.

**Rate limit:** 300 requests per minute

`POST /accounts`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

#### `pylon accounts merge`

Merges one or more accounts into a surviving account. Issues, contacts, opportunities, domains, channels, external IDs, and other associated data are transferred to the surviving account. Tags and custom field values of the merged accounts are not transferred. The merged accounts are permanently deleted. This cannot be undone. Accounts are merged sequentially, each in its own transaction; if a merge fails partway through, accounts already merged are not restored.

**Rate limit:** 30 requests per minute

`POST /accounts/merge`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon accounts search`

Optionally pass `search_text` for fuzzy matching. Results are intersected with any provided filter.

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `id` | `equals`, `in`, `not_in` |
 `domains` | `contains`, `does_not_contain`, `in`, `not_in` |
 `tags` | `contains`, `does_not_contain`, `in`, `not_in` |
 `name` | `equals`, `in`, `not_in`, `string_contains` |
 `external_ids` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `owner_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |

For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute

`POST /accounts/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon accounts update`

Updates an existing account by ID or external ID. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /accounts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon accounts upload-file`

Uploads one or more files to an account by ID or external ID.

**Rate limit:** 30 requests per minute

`POST /accounts/{id}/files`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the account to upload files to. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Timestamp values use RFC3339 format. `object_id` is the ID of the object the entry is
for, matching the `object_id` field of the returned entries.

**Rate limit:** 30 requests per minute

`POST /audit-logs/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon call-recordings`

#### `pylon call-recordings create`

Creates a call recording from your own call recorder. Set app_type to `custom_call_recorder`; the Custom Call Recorder integration must be enabled for your organization, or the request returns 400. start_time, end_time, and at least one call_recording_messages entry are required. Every speaker_email must appear in participant_emails or match primary_user_email. The recording is linked to account_id if provided, otherwise to an account matched from the participant emails. Reusing a recording_id returns the existing recording unchanged.

**Rate limit:** 30 requests per minute

`POST /call-recordings`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Timestamp values use RFC3339 format.

**Rate limit:** 120 requests per minute

`POST /call-recordings/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon call-recordings update`

Updates a call recording by ID. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /call-recordings/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the call recording to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon contacts`

#### `pylon contacts create`

Creates a new contact with the specified email and optional metadata.

**Rate limit:** 300 requests per minute

`POST /contacts`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon contacts search`

Filterable fields and their allowed operators:

 Field | Allowed operators |
 --- | --- |
 `id` | `equals`, `in`, `not_in` |
 `email` | `equals`, `in`, `not_in`, `string_contains` |
 `name` | `equals`, `in`, `not_in`, `string_contains` |
 `account_id` | `equals`, `in`, `not_in` |

For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute

`POST /contacts/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon contacts update`

Updates a contact by ID or external ID. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /contacts/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or external ID of the contact to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon custom-fields`

#### `pylon custom-fields create`

Creates a new custom field definition for the specified object type.

**Rate limit:** 120 requests per minute

`POST /custom-fields`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--object-type` | `account | issue | contact | task | project | meeting | opportunity` | Yes | The object type of the custom fields. Can be "account", "issue", "contact", "task", "project", "meeting", or "opportunity". |

#### `pylon custom-fields update`

Updates a custom field definition. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /custom-fields/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the custom field. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon custom-fields select-options`

#### `pylon custom-fields select-options create`

Adds an option to a select or multiselect custom field.

**Rate limit:** 120 requests per minute

`POST /custom-fields/{id}/select-options`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the custom field. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon custom-objects`

#### `pylon custom-objects bulk-update`

Applies the same update to multiple custom objects of the given type in a single request. Pass between 1 and 100 IDs and the custom field values to set; only the provided fields are modified on each object. To update the linked account, pass the built-in Account relationship field in `custom_fields`: `{"ids":["object_uuid"],"custom_fields":{"account":{"value":"account_uuid"}}}`. To unset a field, pass its slug with an empty value.

**Rate limit:** 120 requests per minute

`PATCH /custom-objects/{type}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "opportunity"). |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon custom-objects create`

Creates a new custom object instance of the given type. To link the object to an account, pass the built-in Account relationship field in `custom_fields`: `{"name":"Example","custom_fields":{"account":{"value":"account_uuid"}}}`.

**Rate limit:** 120 requests per minute

`POST /custom-objects/{type}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

`account` is the built-in Account relationship field present on every custom object type; its values are account IDs.
Timestamp values use RFC3339 format. For custom fields, pass the field slug as `field`.

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon custom-objects update`

Updates a custom object. Only provided fields are modified. To update the linked account, pass the built-in Account relationship field in `custom_fields`: `{"custom_fields":{"account":{"value":"account_uuid"}}}`.

**Rate limit:** 120 requests per minute

`PATCH /custom-objects/{type}/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--type` | `string` | Yes | The type slug of the custom object (e.g. "companies"). |
| `--id` | `string` | Yes | The ID of the custom object. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | Yes | Request body as JSON (or use individual body-field flags) |

#### `pylon feature-requests create`

Creates a new feature request. When should_auto_fetch_evidence is true, supporting evidence is automatically gathered and used to generate the description.

**Rate limit:** 120 requests per minute

`POST /feature-requests`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon feature-requests merge`

Merges one or more feature requests into a surviving feature request. Evidence and linked external issues are consolidated, and merged feature requests are archived. Merge requests that share a target should be sent serially.

**Rate limit:** 30 requests per minute

`POST /feature-requests/merge`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | Yes | Request body as JSON (or use individual body-field flags) |

#### `pylon feature-requests search`

Returns feature requests matching the given criteria. Supports semantic search, status filtering, and pagination.

**Rate limit:** 120 requests per minute

`POST /feature-requests/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon feature-requests set-portal-visibility`

Toggles portal visibility for a set of accounts on a feature request. Idempotent — adding already-visible accounts or removing already-hidden accounts is a no-op. Note: visibility only takes effect when the Feature Requests tab is enabled in portal settings.

**Rate limit:** 120 requests per minute

`POST /feature-requests/{id}/set-portal-visibility`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon feature-requests update`

Updates an existing feature request. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /feature-requests/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the feature request to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon issue-groups`

#### `pylon issue-groups create`

Creates an issue group and attaches its initial child issues atomically.

**Rate limit:** 30 requests per minute

`POST /issue-groups`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon issue-groups children`

#### `pylon issue-groups children add`

Adds one or more child issues atomically. Issues already attached to this group are ignored.

**Rate limit:** 120 requests per minute

`POST /issue-groups/{issue_group_id}/children`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--issue-group-id` | `string` | Yes | The ID of the issue group. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues create`

Creates a new issue and its first message. Requires either an account_id or requester information.

Requester fields identify the customer, user_id or contact_id identifies the first-message author, and destination_metadata controls delivery. These choices are independent. If destination_metadata is omitted, the first message is an internal note and no customer is contacted. See the request-field descriptions and examples for destination-specific requirements.

**Rate limit:** 30 requests per minute

`POST /issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues create-ai-response`

Generates an AI response for the specified issue using the given agent.

**Rate limit:** 120 requests per minute

`POST /issues/{id}/ai-response`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to create an AI response for. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues create-draft-reply`

Creates a private customer-reply draft without sending it. The draft is visible only to its owner and may require a normal issue refetch before appearing in the app. For unlinked or service API tokens, user_id is required. This endpoint updates only untouched drafts that it previously created; every other existing draft returns a conflict.

**Rate limit:** 30 requests per minute

`POST /issues/{id}/draft-reply`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue. |
| `--json` | `JSON` | Yes | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues link-external-issue`

By default, links external issues. To unlink issues, set the operation field to "unlink".

**Rate limit:** 120 requests per minute

`POST /issues/{id}/external-issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to link external issues to. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues merge`

Merges one or more issues into a primary issue. All issues must belong to the same account (or, without an account, the same requester). All issues are found and validated before anything changes, so a request rejected for a missing or ineligible issue merges nothing. Closing messages are sent before the merge and are not recalled: if sending one fails, or the merge fails afterwards, duplicates processed earlier may already have received it. This cannot be undone.

**Rate limit:** 30 requests per minute

`POST /issues/merge`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues reply`

Sends a customer-facing reply on an issue, visible to the requester.

message_id is required to identify which existing customer-visible conversation or thread to continue. Use the top-level message id returned by GET /issues/{id}/messages; do not use an external provider's message ID or the nested email_info.message_id value.

For an email conversation, email_info must contain at least one recipient across to_emails, cc_emails, and bcc_emails. The referenced message controls email threading, but its recipients are not copied automatically.

**Rate limit:** 30 requests per minute

`POST /issues/{id}/reply`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
 `tags` | `contains`, `does_not_contain`, `in`, `not_in` |
 `title` | `string_contains`, `string_does_not_contain` |
 `body_html` | `string_contains`, `string_does_not_contain` |
 `assignee_id` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `team_id` | `equals`, `in`, `not_in` |
 `issue_type` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `issue_is_issue_group` | `equals`, `in`, `not_in` |
 `resolved_at` | `time_is_after`, `time_is_before`, `time_range` |
 `latest_message_activity_at` | `time_is_after`, `time_is_before`, `time_range` |
 `updated_at` | `time_is_after`, `time_is_before`, `time_range` |
 `slack_channel_id` | `equals`, `in`, `not_in` |
 `workspace_email` | `equals`, `in`, `not_in`, `is_set`, `is_unset` |
 `reopened` | `equals`, `in`, `not_in` |

Timestamp values use RFC3339 format. Standard `state` values are `new`, `waiting_on_you`, `waiting_on_customer`, `on_hold`, and `closed`; custom status slugs are also supported. `issue_type` values are `conversation` and `ticket`.

For tag filters, pass the tag name. For custom fields, pass the field slug as `field`. `slack_channel_id` identifies the Slack channel where the issue was created. `workspace_email` identifies the email address connected to the Pylon workspace through which the issue's email conversation is routed. `customer_portal_visible` values are `true` and `false`; issue groups are never visible in the customer portal, so they always match `false`. `reopened` values are `true` and `false`; it is a sticky flag set the first time an issue is reopened after being resolved, and it records no timestamp.

**Rate limit:** 120 requests per minute

`POST /issues/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues snooze`

Snoozes an issue until the specified date and time.

**Rate limit:** 120 requests per minute

`POST /issues/{id}/snooze`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to snooze. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon issues update`

Updates an existing issue. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /issues/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon issues followers`

#### `pylon issues followers add`

By default, adds followers. To remove followers, set the operation field to "remove".

**Rate limit:** 120 requests per minute

`POST /issues/{id}/followers`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID or number of the issue to add followers to. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

To post a reply, use the message's top-level id—not thread_id or email_info.message_id. To post an internal note, use an internal thread's thread_id or an internal note's top-level id. Omit both limit and cursor to return all messages; when cursor is provided without limit, the page size defaults to 100.

**Rate limit:** 120 requests per minute

`GET /issues/{id}/messages`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue to fetch messages for. |
| `--cursor` | `string` | No | The cursor to use for pagination. |
| `--limit` | `integer (int64)` | No | The number of messages to fetch. Must be greater than 0 and at most 1000. If omitted, all messages are returned for backward compatibility. |

#### `pylon issues messages redact`

Permanently replaces a message's stored content with redacted_body_message and optionally deletes its attachments. This action cannot be undone.
When omitted, redacted_body_message defaults to "This message has been redacted." and redact_attachments defaults to true.

**Rate limit:** 120 requests per minute

`POST /issues/{id}/messages/{message_id}/redact`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the issue that the message belongs to. |
| `--message-id` | `string` | Yes | The ID of the message to redact. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Returns voice call records for the specified phone issue. Each call includes its recordings, with parsed transcript segments and a presigned download URL for the audio file. Recordings whose transcript has not yet completed are omitted; refetch later to see them.

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--media` | `all | none` | No | Controls whether embedded media is included in article HTML. Valid values are all (default) and none. When set to none, embedded images, video, audio, and inline media are removed while descriptive text and standard links are preserved. |

#### `pylon knowledge-bases articles request-review`

Requests human and/or AI review on the article's current draft version. At least one of `reviewer_user_ids` or `request_ai_review` must be provided. The article must have an unpublished current version. Requesting AI review requires the organization to have AI article review enabled.

**Rate limit:** 30 requests per minute

`POST /knowledge-bases/{id}/articles/{article_id}/request-review`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the article belongs to. |
| `--article-id` | `string` | Yes | The ID of the article to request review for. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon knowledge-bases articles update`

Updates an existing article. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /knowledge-bases/{id}/articles/{article_id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The KnowledgeBaseID of the article to update. |
| `--article-id` | `string` | Yes | The ID of the article to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon knowledge-bases collections`

#### `pylon knowledge-bases collections create`

Creates a new collection within a knowledge base.

**Rate limit:** 30 requests per minute

`POST /knowledge-bases/{id}/collections`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the article is being added to. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon knowledge-bases route-redirects`

#### `pylon knowledge-bases route-redirects create`

Creates a path redirect within a knowledge base, mapping a source path to an article or collection.

**Rate limit:** 30 requests per minute

`POST /knowledge-bases/{id}/route-redirects`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the knowledge base the route redirect is being added to. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | Yes | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Timestamp values use RFC3339 format. Milestones belonging to an unlaunched project are not returned.

**Rate limit:** 120 requests per minute

`POST /milestones/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon milestones update`

Updates an existing milestone. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /milestones/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the milestone to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon projects`

#### `pylon projects create`

Creates a new project for an account. Provide a name or project_template_id. A template supplies defaults; non-empty name and description_html values and supplied ai_instructions, customer_portal_visible, and owner_id values override them. Supplying either start_date or end_date replaces both template dates.

**Rate limit:** 300 requests per minute

`POST /projects`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Timestamp values use RFC3339 format. Valid `status` values are `not_started`, `in_progress`, and `completed`. For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute

`POST /projects/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon projects update`

Updates an existing project. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /projects/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the project to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Timestamp values use RFC3339 format.

**Rate limit:** 120 requests per minute

`POST /surveys/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon tags update`

Updates an existing tag. Only provided fields are modified.

**Rate limit:** 30 requests per minute

`PATCH /tags/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the tag to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon tasks link-issue`

Links the issue to the task by default. To unlink it, set the operation field to "unlink".

**Rate limit:** 120 requests per minute

`POST /tasks/{id}/issues`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to link a Pylon issue to. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Timestamp values use RFC3339 format. Valid `status` values are `not_started`, `in_progress`, and `completed`. For custom fields, pass the field slug as `field`.

**Rate limit:** 120 requests per minute

`POST /tasks/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon tasks update`

Updates an existing task. Only provided fields are modified.

**Rate limit:** 300 requests per minute

`PATCH /tasks/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon tasks comments`

#### `pylon tasks comments create`

Creates a new comment on a task. The authenticated user is the author.

**Rate limit:** 120 requests per minute

`POST /tasks/{id}/comments`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the task to add a comment to. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon teams`

#### `pylon teams create`

Creates a new team with a name and optional member list. Optionally sets how the team
assigns issues and creates its recurring assignment schedule in the same call.

**Rate limit:** 30 requests per minute

`POST /teams`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

---

### `pylon training-data`

#### `pylon training-data create`

Creates a new training data configuration for the organization.

**Rate limit:** 30 requests per minute

`POST /training-data`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon training-data upload-files`

Uploads one or more files to a training data configuration.

**Rate limit:** 30 requests per minute

`POST /training-data/upload`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

Returns all user roles for the organization.

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

**Rate limit:** 120 requests per minute

`POST /users/search`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

#### `pylon users update`

Updates an existing user. Only provided fields are modified.

**Rate limit:** 120 requests per minute

`PATCH /users/{id}`

| Flag | Type | Required | Description |
|------|------|----------|-------------|
| `--id` | `string` | Yes | The ID of the user to update. |
| `--json` | `JSON` | No | Request body as JSON (or use individual body-field flags) |

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

# Operational Status

Project: Clinic Booking Mini

Task: CBM-004

State: REVIEW

READY:

CBM-001 Remote DONE: declared at commit `4796bc9`

CBM-002 Remote DONE: declared at commit `20e91a3`

CBM-003 Remote DONE: declared at commit `425df38`

CBM-004 Local DONE: not declared

CBM-004 Remote DONE: not declared

## Current Scope

CBM-004 registers the scheduling models in Django Admin with simple `ModelAdmin` classes.

Allowed scope:

- `scheduling/admin.py`
- Operational documentation updates
- Django validation

## Execution Boundary

Allowed:

- Register `Client`
- Register `Service`
- Register `Professional`
- Register `Appointment`
- Simple `ModelAdmin` options:
  - `list_display`
  - `list_filter`
  - `search_fields`
  - `ordering`
  - `readonly_fields` for `created_at` and `updated_at`

Blocked:

- Changes to `scheduling/models.py`.
- Migrations.
- `makemigrations`.
- `migrate`.
- Settings, URLs, templates, views, forms, APIs, auth, seed data, deployment, package, or dependency changes.
- Real patient data or sensitive health data.
- Commit.
- Push.
- Opening CBM-005 automatically.

## Review State

CBM-004 remains in REVIEW until the Trigger explicitly approves Local DONE and any controlled commit.

READY remains empty.

CBM-005 remains not started and not opened.

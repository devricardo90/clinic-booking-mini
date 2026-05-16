# Operational Status

Project: Clinic Booking Mini

Task: CBM-009

State: REVIEW

READY:

CBM-001 through CBM-008: Remote DONE

CBM-009 Local DONE: not declared

CBM-009 Remote DONE: not declared

## Current Scope

CBM-009 adds a basic conflict guard to the existing public appointment request flow.

Implemented scope:

- Validation blocks a request when an existing appointment has the same professional and the same scheduled date/time.
- The existing public form displays a clear conflict message.
- A different time for the same professional remains allowed.
- Tests cover both paths.

## Validation State

Validation evidence is collected in the session output:

- `python manage.py check`
- `python manage.py test scheduling`
- Manual public flow validation by HTTP POST and shell query
- `git diff --check`

## Explicit Limits

- No UI redesign.
- No advanced calendar.
- No new admin panel.
- No authentication.
- No REST API.
- No database schema changes.
- No migrations.
- No global settings changes.
- No deployment.
- No commit.
- No push.

## Review State

CBM-009 remains in REVIEW until the Trigger approves Local DONE and any controlled commit.

READY remains empty.

CBM-010 remains not started and not opened.

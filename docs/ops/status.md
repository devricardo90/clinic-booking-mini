# Operational Status

Project: Clinic Booking Mini

Task: CBM-010

State: REVIEW

READY:

CBM-001 through CBM-009: Remote DONE

CBM-010 Local DONE: not declared

CBM-010 Remote DONE: not declared

## Current Scope

CBM-010 adds a simple operational time guard to the existing public appointment request flow.

Implemented scope:

- Block scheduled times in the past.
- Block Saturday and Sunday.
- Block starts before 08:00.
- Use `Service.duration_minutes` to block appointments ending after 18:00.
- Keep the CBM-009 conflict guard active.
- Add proportional automated tests.

## Validation State

Validation evidence is collected in the session output:

- `python manage.py check`
- `python manage.py test scheduling`
- Manual public flow validation by HTTP POST and shell query
- `git diff --check`

## Explicit Limits

- No UI redesign.
- No advanced calendar.
- No per-professional availability.
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

CBM-010 remains in REVIEW until the Trigger approves Local DONE and any controlled commit.

READY remains empty.

CBM-011 remains not started and not opened.

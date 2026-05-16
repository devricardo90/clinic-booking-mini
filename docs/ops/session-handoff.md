# Session Handoff

Project: Clinic Booking Mini

Task: CBM-008

State: Local DONE pending commit

## Starting Point

CBM-007 is Remote DONE at commit `0f2f137`.

The project has a public homepage, Django Admin, idempotent demo seed data, and read-only public overview data.

## What Was Done

CBM-008 adds a minimal public appointment request flow:

- `/appointments/new/`
- `/appointments/success/`
- `AppointmentRequestForm`
- Client creation/reuse by email
- Appointment creation with status `SCHEDULED`
- Public homepage link to the appointment request form

## Validation

- `python manage.py check` passed.
- `python manage.py seed_demo_data` passed.
- Browser smoke passed: home 200, form 200, POST 302, success 200, admin login 200.
- Appointment was created for `cbm008.smoke@example.com`.

## Important Limits

- No availability engine.
- No conflict prevention.
- No cancellation flow.
- No email sending.
- No payment flow.
- No API.
- No public login.
- `db.sqlite3` and `__pycache__` are outside Git.

## Current State

- CBM-008 is Local DONE pending controlled commit.
- READY is empty.
- CBM-008 Remote DONE is not declared.
- No push has been made for CBM-008.
- CBM-009 has not been opened.

## Suggested Next Step

Create the controlled CBM-008 commit only after explicit authorization.

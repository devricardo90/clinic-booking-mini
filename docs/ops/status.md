# Operational Status

Project: Clinic Booking Mini

Task: CBM-008

State: Local DONE pending commit

READY:

CBM-001 through CBM-007: Remote DONE

CBM-008 Local DONE: validated, pending controlled commit

CBM-008 Remote DONE: not declared

## Current Scope

CBM-008 adds the first minimal public appointment request flow.

Implemented scope:

- Public route `/appointments/new/`.
- Public route `/appointments/success/`.
- `AppointmentRequestForm`.
- Client creation/reuse by email.
- Appointment creation with status `SCHEDULED`.
- Public homepage link to request an appointment.

## Validation State

- `python manage.py check` passed.
- `python manage.py seed_demo_data` passed.
- Browser smoke passed:
  - home 200
  - form 200
  - POST 302
  - success 200
  - admin login 200
- Appointment created for `cbm008.smoke@example.com`.

## Explicit Limits

- No availability engine.
- No conflict prevention.
- No cancellation flow.
- No email sending.
- No payment flow.
- No API.
- No public login.
- `db.sqlite3` and `__pycache__` are outside Git.

## Current Operational State

CBM-008 is Local DONE pending controlled commit.

READY remains empty.

CBM-009 remains not started and not opened.

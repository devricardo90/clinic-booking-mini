# Clinic Booking Mini Status

Project: Clinic Booking Mini

Runtime context: official RIC Local Orchestrator runtime, `ric-orchestrator-runtime:latest`

Current item: CBM-008

Current state: Local DONE pending commit

READY:

CBM-001 through CBM-007: Remote DONE

CBM-008 Local DONE: validated, pending controlled commit

CBM-008 Remote DONE: not declared

## Summary

CBM-008 implements the minimal public appointment request flow.

Implemented scope:

- Public route `/appointments/new/`.
- Public route `/appointments/success/`.
- `AppointmentRequestForm`.
- Client creation/reuse by email.
- Appointment creation with status `SCHEDULED`.
- Public homepage link to request an appointment.

## Validation

- `python manage.py check` passed.
- `python manage.py seed_demo_data` passed.
- Browser smoke passed: home 200, form 200, POST 302, success 200, admin login 200.
- Appointment was created for `cbm008.smoke@example.com`.

## Explicit Limits

- No availability engine.
- No conflict prevention.
- No cancellation flow.
- No email sending.
- No payment flow.
- No API.
- No public login.
- `db.sqlite3` and `__pycache__` remain outside Git.

CBM-009 remains not opened.

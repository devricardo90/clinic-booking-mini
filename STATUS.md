# Clinic Booking Mini Status

Project: Clinic Booking Mini

Runtime context: official RIC Local Orchestrator runtime, `ric-orchestrator-runtime:latest`

Last completed: CBM-014

Current item: CBM-015

Current state: REVIEW

READY:

CBM-001 through CBM-014: Remote DONE

CBM-015 Local DONE: not declared

CBM-015 Remote DONE: not declared

## Summary

CBM-015 implements the basic appointment lifecycle actions following CBM-014.

Implemented scope:

- Appointment.Status: added PENDING and REJECTED. Default changed to PENDING.
- Migration 0002 created for model change.
- Public form now creates Appointment in PENDING state.
- Admin action confirm_pending: PENDING → SCHEDULED with conflict revalidation.
- Admin action reject_pending: PENDING → REJECTED (only from PENDING; skips others).
- Existing mark_scheduled and mark_canceled retained.
- has_scheduling_conflict() extracted to forms.py for reuse by admin.
- 18 tests pass (12 existing updated + 6 new).

## Explicit Limits

- No email.
- No notifications.
- No patient portal.
- No public login.
- No REST API.
- No payment.
- No deployment.
- No dependency changes.
- No commit or push without Trigger authorization.

CBM-016 remains not opened.

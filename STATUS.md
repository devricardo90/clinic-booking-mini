# Clinic Booking Mini Status

Project: Clinic Booking Mini

Runtime context: official RIC Local Orchestrator runtime, `ric-orchestrator-runtime:latest`

Last completed: CBM-015 (commit 06664b0)

Current item: CBM-016

Current state: READY

READY: CBM-016 — Improve Appointment Admin Visibility After Lifecycle

CBM-001 through CBM-015: Remote DONE

CBM-016 Local DONE: not declared

CBM-016 Remote DONE: not declared

## Summary

CBM-016 will improve AppointmentAdmin visibility after the lifecycle actions introduced
in CBM-015. The admin list currently shows limited fields and does not surface PENDING or
REJECTED statuses clearly for the operator.

Authorized implementation scope (execution pending):

- Improve AppointmentAdmin list_display with status, client, service, professional, datetime.
- Add list_filter by status, service, professional, and date.
- Add or extend search_fields using existing model fields only.
- Preserve all existing lifecycle actions (confirm_pending, reject_pending, mark_scheduled, mark_canceled).
- Update operational docs on completion.

## Explicit Limits

- No model changes.
- No migrations.
- No forms.py changes.
- No views.py changes.
- No availability rule changes.
- No public frontend.
- No email.
- No authentication.
- No deployment.
- No commit or push without Trigger authorization.

CBM-017 remains not opened.

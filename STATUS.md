# Clinic Booking Mini Status

Project: Clinic Booking Mini

Runtime context: official RIC Local Orchestrator runtime, `ric-orchestrator-runtime:latest`

Current item: CBM-010

Current state: REVIEW

READY:

CBM-001 through CBM-009: Remote DONE

CBM-010 Local DONE: not declared

CBM-010 Remote DONE: not declared

## Summary

CBM-010 adds a public appointment request time guard.

Implemented scope:

- Blocks appointments in the past.
- Blocks Saturday and Sunday appointments.
- Blocks appointments starting before 08:00.
- Uses `Service.duration_minutes` to block appointments that finish after 18:00.
- Keeps the CBM-009 same-professional/same-date-time conflict guard intact.
- Adds focused tests for the time guard and existing conflict guard.

## Explicit Limits

- No UI redesign.
- No advanced calendar.
- No per-professional availability.
- No new admin panel.
- No authentication.
- No REST API.
- No database schema changes or migrations.
- No global settings changes.
- No deployment.
- No commit or push.

CBM-011 remains not opened.

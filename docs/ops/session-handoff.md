# Session Handoff

Project: Clinic Booking Mini

Last completed: CBM-014

Current item: CBM-015

State: REVIEW

## Starting Point

CBM-014 is Remote DONE. docs/product/appointment-lifecycle.md exists and defines the
official lifecycle: PENDING → SCHEDULED or REJECTED; SCHEDULED → CANCELED;
only SCHEDULED blocks availability.

The model before CBM-015 had: SCHEDULED, CANCELED (default: SCHEDULED).

## What Was Done

CBM-015 implements the basic appointment lifecycle actions:

- Appointment.Status: PENDING, SCHEDULED, CANCELED, REJECTED. Default: PENDING.
- Migration 0002 created (AlterField: choices + default).
- Public appointment_new: creates Appointment in PENDING.
- has_scheduling_conflict() extracted into forms.py module scope (reused by admin).
- Admin confirm_pending: PENDING → SCHEDULED with conflict revalidation at confirmation time.
- Admin reject_pending: PENDING → REJECTED (skips non-PENDING with warning).
- mark_scheduled (CANCELED → SCHEDULED) and mark_canceled unchanged.
- 18 tests: 12 updated + 6 new. All passing.

## Key Design Decisions

- PENDING does not block availability (CBM-014: "To be defined"; task instruction: if only SCHEDULED
  blocks, revalidate conflict on confirmation). Confirmed approach: PENDING does not block.
- Conflict guard in the public form still runs against SCHEDULED (immediate UX feedback if slot taken).
- Conflict is revalidated when admin confirms PENDING → SCHEDULED; confirmation fails if slot blocked.
- SCHEDULED → REJECTED is prohibited by design: reject_pending skips non-PENDING appointments.
- Templates unchanged: success page uses get_status_display(), which now shows "Pending".

## Important Boundary

No email, notifications, patient portal, login, REST API, payment, or deployment.
No COMPLETED or NO_SHOW states. No CBM-016 opened.
No commit or push without Trigger authorization.

## Current State

- CBM-015 is in REVIEW.
- READY is empty.
- CBM-015 Local DONE is not declared.
- CBM-015 Remote DONE is not declared.
- No commit has been made for CBM-015.
- No push has been made for CBM-015.
- CBM-016 has not been opened.

## Suggested Next Review

Review scheduling/models.py, scheduling/admin.py, scheduling/forms.py, scheduling/views.py,
scheduling/tests.py, and migration 0002 before approving CBM-015 for Local DONE and a
controlled commit.

# Session Handoff

Project: Clinic Booking Mini

Last completed: CBM-013

Current item: CBM-014

State: REVIEW

## Starting Point

CBM-013 is Remote DONE at commit `0e71035`.

The project has a public appointment request flow with overlap-aware availability guards,
a success summary page, and admin lifecycle actions (mark_scheduled, mark_canceled).
The `Appointment.Status` model has two values: SCHEDULED and CANCELED.

## What Was Done

CBM-014 creates the official appointment lifecycle documentation:

- docs/product/appointment-lifecycle.md created.
- Official states defined: SCHEDULED and CANCELED (current MVP); PENDING and REJECTED (planned future).
- Transitions documented: public form → SCHEDULED; admin mark_canceled → CANCELED; admin mark_scheduled → SCHEDULED.
- Prohibited transitions defined: SCHEDULED → REJECTED explicitly prohibited; CANCELED → REJECTED prohibited.
- Availability impact documented: only SCHEDULED blocks availability and is checked by the conflict guard.
- Responsibility matrix documented: public user submits; admin approves, cancels.
- MVP boundaries documented: no patient confirmation, no direct rescheduling, no COMPLETED, no NO_SHOW.
- Future evolution notes documented.

## Important Boundary

No code was changed. No model, form, view, admin, test, migration, template, or URL was altered.
No COMPLETED or NO_SHOW states were introduced. No CBM-015 was opened.
No commit or push without Trigger authorization.

## Current State

- CBM-014 is in REVIEW.
- READY is empty.
- CBM-014 Local DONE is not declared.
- CBM-014 Remote DONE is not declared.
- No commit has been made for CBM-014.
- No push has been made for CBM-014.
- CBM-015 has not been opened.

## Suggested Next Review

Review docs/product/appointment-lifecycle.md for accuracy against the current model and
admin actions before approving CBM-014 for Local DONE and a controlled commit.

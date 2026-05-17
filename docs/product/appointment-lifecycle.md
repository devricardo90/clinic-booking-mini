# Appointment Lifecycle

Project: Clinic Booking Mini

Task: CBM-015

State: REVIEW

## Purpose

This document defines the official lifecycle of an Appointment in the Clinic Booking Mini MVP.
It establishes the states, permitted and prohibited transitions, actor responsibilities, and
availability impact of each state.

Last updated: CBM-015 — aligned to the implemented code as of this task.

---

## Official States

All four states below are implemented in `Appointment.Status` (`scheduling/models.py`).

| State | Value | Description |
|---|---|---|
| `PENDING` | `"PENDING"` | Request submitted by the public user, awaiting administrative decision. Default state on creation. Does not block availability. |
| `SCHEDULED` | `"SCHEDULED"` | Confirmed by admin. Active appointment. Blocks availability. |
| `CANCELED` | `"CANCELED"` | Canceled by admin from SCHEDULED. Does not block availability. Retained in the database for audit. |
| `REJECTED` | `"REJECTED"` | Rejected by admin from PENDING only. Request was denied before being scheduled. Does not block availability. |

> Note on CBM-001 original scope: The original `business-rules.md` and `mvp-scope.md`
> documented `COMPLETED` and `NO_SHOW` as MVP states. Neither was implemented in any
> CBM. Both remain out of scope until a future Trigger approval explicitly authorizes
> their implementation.

---

## Transitions

### Implemented

```
[Public Form Submit] ──────────────────────────► PENDING
                                                    │
                  Admin: confirm_pending            │
PENDING ────────────────────────────────────────► SCHEDULED
                                                    │
                  Admin: mark_canceled              │
SCHEDULED ──────────────────────────────────────► CANCELED
                                                    │
                  Admin: mark_scheduled             │
CANCELED ───────────────────────────────────────► SCHEDULED
                                                    │
                  Admin: reject_pending             │
PENDING ────────────────────────────────────────► REJECTED
```

### Detailed Rules

- **[Public Form Submit] → PENDING**
  The public `AppointmentRequestForm` creates an `Appointment` record with
  `status=Appointment.Status.PENDING` (model default). The form enforces all
  availability guards (time guards, working hours, overlap against SCHEDULED slots)
  before the record is created. The request waits for administrative review.

- **PENDING → SCHEDULED** (`confirm_pending`)
  Admin selects one or more PENDING appointments in Django Admin and applies
  `confirm_pending`. Before transitioning, the action revalidates the conflict guard
  against currently SCHEDULED appointments. If a conflict is detected at confirmation
  time, the appointment remains PENDING and admin receives a warning. If no conflict,
  the appointment is marked SCHEDULED.

- **PENDING → REJECTED** (`reject_pending`)
  Admin selects one or more PENDING appointments and applies `reject_pending`.
  The transition is immediate. Non-PENDING appointments selected in the same batch
  are skipped with a warning. REJECTED is a terminal state in the current MVP.

- **SCHEDULED → CANCELED** (`mark_canceled`)
  Admin applies `mark_canceled`. The transition is immediate and requires no
  confirmation. The canceled slot becomes available immediately for new bookings.

- **CANCELED → SCHEDULED** (`mark_scheduled`)
  Admin applies `mark_scheduled` to reactivate a canceled appointment. The conflict
  guard is not re-evaluated on reactivation; admin is responsible for checking
  availability before reactivating.

---

## Prohibited Transitions

| Transition | Status | Reason |
|---|---|---|
| `SCHEDULED → REJECTED` | **Explicitly prohibited** | REJECTED is reserved for requests that have not yet been approved (PENDING only). After scheduling, the correct reversal is CANCELED. The `reject_pending` action enforces this by skipping non-PENDING appointments. |
| `CANCELED → REJECTED` | **Prohibited** | A canceled appointment is already resolved and cannot re-enter a review queue. |
| `REJECTED → any state` | **Not supported in current MVP** | REJECTED is a terminal state. No reactivation or re-submission path exists in the current MVP. |
| `PENDING → CANCELED` | **Not supported** | PENDING requests are resolved via confirm (→ SCHEDULED) or reject (→ REJECTED). Cancellation applies only to SCHEDULED appointments. |

---

## Availability Impact

Only `SCHEDULED` appointments block availability. The overlap condition used by the
conflict guard (`forms.py`, `has_scheduling_conflict()`):
`existing_start < new_end AND existing_end > new_start`.

| State | Blocks Availability | Checked by Conflict Guard |
|---|---|---|
| `PENDING` | **No** | No — PENDING requests do not hold the slot. A slot can receive multiple PENDING requests simultaneously. |
| `SCHEDULED` | **Yes** | **Yes** — checked at public form submission and re-checked at `confirm_pending`. |
| `CANCELED` | No | No — slot is immediately reusable after cancellation. |
| `REJECTED` | No | No — rejected request never held the slot. |

### Conflict revalidation at confirmation

Because PENDING does not block availability, two PENDING requests for the same slot can
coexist. When admin confirms one, it becomes SCHEDULED. If admin then tries to confirm
the second, `confirm_pending` detects the conflict against the now-SCHEDULED appointment
and leaves the second request in PENDING with a warning.

---

## Responsibility Matrix

| Action | Actor | Mechanism | Implemented |
|---|---|---|---|
| Submit appointment request | Public (anonymous user) | Public form (`AppointmentRequestForm`) | YES |
| Confirm pending request | Admin | Django Admin action `confirm_pending` | YES |
| Reject pending request | Admin | Django Admin action `reject_pending` | YES |
| Cancel scheduled appointment | Admin | Django Admin action `mark_canceled` | YES |
| Reactivate canceled appointment | Admin | Django Admin action `mark_scheduled` | YES |

---

## MVP Boundaries

The following are explicitly out of scope for the current MVP:

- Patient or client confirmation of appointment (no confirmation step exists).
- Direct rescheduling by admin (admin must cancel the existing appointment and create a new one).
- Conflict guard re-evaluation on `mark_scheduled` reactivation (CANCELED → SCHEDULED).
- Reactivation path for REJECTED appointments.
- `COMPLETED` state (not implemented; not authorized).
- `NO_SHOW` state (not implemented; not authorized).
- Email notifications of any kind.
- Token-based or link-based access for clients.
- REST API endpoints.

---

## Future Evolution Notes

The following require explicit Trigger approval and a dedicated CBM before implementation:

- Patient confirmation flow.
- Direct rescheduling (single admin action without cancel-and-recreate).
- Conflict guard re-evaluation on reactivation (`CANCELED → SCHEDULED`).
- Reactivation or re-submission path for REJECTED requests.
- `COMPLETED` and `NO_SHOW` states (documented in CBM-001 scope but not implemented).

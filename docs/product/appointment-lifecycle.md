# Appointment Lifecycle

Project: Clinic Booking Mini

Task: CBM-014

State: REVIEW

## Purpose

This document defines the official lifecycle of an Appointment in the Clinic Booking Mini MVP.
It establishes the states, permitted and prohibited transitions, actor responsibilities, and
availability impact of each state. It separates what is implemented in the current MVP from
what belongs to planned future tasks.

---

## Official States

### MVP Current — Implemented in `Appointment.Status`

These are the states present in the Django model (`scheduling/models.py`, as of CBM-013):

| State | Value | Description |
|---|---|---|
| `SCHEDULED` | `"SCHEDULED"` | Active appointment. Created immediately when a public request passes all validation guards. Blocks availability. |
| `CANCELED` | `"CANCELED"` | Appointment canceled by admin. Does not block availability. Retained in the database for audit and agenda context. |

### Planned Future States — Not Implemented in the Current Model

These states are defined at the product level for a future CBM. They do not exist in the
current `Appointment.Status` TextChoices and require a model change, migration, form update,
and admin action update before they can be used.

| State | Description |
|---|---|
| `PENDING` | Request submitted but not yet reviewed by admin. Would precede SCHEDULED or REJECTED. |
| `REJECTED` | Request denied while still in PENDING. Cannot be applied to a SCHEDULED appointment. |

> Note on CBM-001 original scope: The original `business-rules.md` and `mvp-scope.md`
> documented `COMPLETED` and `NO_SHOW` as MVP states. Neither was implemented in any
> subsequent CBM. Both remain out of scope until a future Trigger approval explicitly
> authorizes their implementation.

---

## Transitions

### MVP Current — Implemented

```
[Public Form Submit] ──────────────────────────► SCHEDULED
                                                    │
                     Admin: mark_canceled           │
SCHEDULED ─────────────────────────────────────► CANCELED
                                                    │
                     Admin: mark_scheduled           │
CANCELED ──────────────────────────────────────► SCHEDULED
```

Detailed rules:

- **[Public Form Submit] → SCHEDULED**
  The public `AppointmentRequestForm` creates an `Appointment` record with
  `status=Appointment.Status.SCHEDULED` as the default. No admin review step exists
  in the current MVP. The form enforces all availability guards before the record is
  created (time guards, working hours, overlap guard).

- **SCHEDULED → CANCELED**
  Admin selects one or more SCHEDULED appointments in Django Admin and applies
  the `mark_canceled` action. The transition is immediate and requires no confirmation.

- **CANCELED → SCHEDULED**
  Admin applies the `mark_scheduled` action to a CANCELED appointment to reactivate it.
  The conflict guard is not re-evaluated on reactivation in the current MVP; admin is
  responsible for checking availability before reactivating.

### Planned Future — Not Implemented

```
[Public Form Submit] ──► PENDING ──► SCHEDULED
                                │
                                └──► REJECTED
```

These transitions require explicit Trigger approval and a new CBM before implementation.

---

## Prohibited Transitions

| Transition | Status | Reason |
|---|---|---|
| `SCHEDULED → REJECTED` | **Explicitly prohibited** | REJECTED is reserved for requests that have not yet been approved. After scheduling, the correct reversal is CANCELED. |
| `CANCELED → REJECTED` | **Prohibited** | A canceled appointment is already resolved and cannot re-enter a review queue. |
| Any state → `PENDING` | **Not applicable in current MVP** | PENDING does not exist in the current model. |

---

## Availability Impact

Only `SCHEDULED` appointments are considered by the conflict guard (`forms.py`). The overlap
condition is: `existing_start < new_end AND existing_end > new_start`.

| State | Blocks Availability | Checked by Conflict Guard |
|---|---|---|
| `SCHEDULED` | **YES** | **YES** |
| `CANCELED` | No | No |
| `PENDING` (future) | To be defined | Not implemented |
| `REJECTED` (future) | No | Not applicable |

A `CANCELED` slot is explicitly reusable: canceling an appointment frees the time slot for
new bookings immediately, without any manual intervention.

---

## Responsibility Matrix

| Action | Actor | Mechanism | Implemented |
|---|---|---|---|
| Submit appointment request | Public (anonymous user) | Public form (`AppointmentRequestForm`) | YES |
| Approve / mark as scheduled | Admin | Django Admin action `mark_scheduled` | YES |
| Cancel appointment | Admin | Django Admin action `mark_canceled` | YES |
| Reject a pending request | Admin | Not yet available | NO (future) |

---

## MVP Boundaries

The following are explicitly out of scope for the current MVP:

- Patient or client confirmation of appointment (no confirmation step exists).
- Direct rescheduling by admin (admin must cancel the existing appointment and create a new one).
- `COMPLETED` state (not implemented; not authorized for this CBM).
- `NO_SHOW` state (not implemented; not authorized for this CBM).
- Email notifications of any kind.
- Token-based or link-based access for clients.
- REST API endpoints.
- Conflict guard re-evaluation on admin reactivation.

---

## Future Evolution Notes

The following require explicit Trigger approval and a dedicated CBM before implementation:

- `PENDING` state: requires model change, migration, form update, admin action update,
  and conflict guard review to determine whether PENDING appointments should block availability.
- `REJECTED` state: same dependencies as PENDING.
- Patient confirmation flow.
- Direct rescheduling (single admin action without cancel-and-recreate).
- `COMPLETED` and `NO_SHOW` states (documented in CBM-001 scope but not implemented).
- Conflict guard re-evaluation on reactivation (`CANCELED → SCHEDULED`).

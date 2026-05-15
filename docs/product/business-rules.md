# Business Rules

Project: Clinic Booking Mini

Task: CBM-001

State: Local DONE

## Safety Boundary

The system is administrative-only. It must not store diagnosis, prescription, treatment records, clinical notes, anamnesis, imaging, medical documents, real patient data, or sensitive health data.

All sample data for the MVP must be fictitious.

## Client Rules

- A client represents a fictitious person who can be scheduled for an appointment.
- Client data should be limited to administrative contact and identification fields required for booking.
- Client records must not include health history, treatment history, documents, or clinical notes.

## Service Rules

- A service represents an administrative booking option.
- A service should have a name, optional description, duration, and active/inactive state.
- Service examples include:
  - Initial evaluation
  - Dental cleaning
  - Whitening consultation
  - Facial harmonization consultation
  - Botox consultation
- Service descriptions must remain administrative and must not capture clinical findings or treatment records.

## Professional Rules

- A professional represents a fictitious provider who can receive appointments.
- Professional data should support scheduling only.
- Professional records should not include credentials verification, medical licensing workflow, payroll, or sensitive HR records in the MVP.

## Appointment Rules

- An appointment links one client, one service, one professional, a date, a start time, and a status.
- An appointment starts as SCHEDULED.
- A SCHEDULED appointment can be changed to COMPLETED, CANCELED, or NO_SHOW.
- A CANCELED appointment remains visible for audit and agenda context.
- A COMPLETED appointment only confirms administrative attendance completion. It does not imply clinical outcome, diagnosis, or treatment record.
- A NO_SHOW appointment means the client did not attend.

## Agenda Rules

- The daily agenda lists appointments for a selected date.
- The daily agenda should show date, time, client display name, service, professional, and status.
- The agenda should be useful for front desk operations and should not show clinical content.

## MVP Constraints

- Local MVP storage should use SQLite.
- The web UI should use Django templates and basic CSS in a later implementation task.
- No external frontend framework is needed for MVP.
- No payment, messaging, or authentication workflows are included in this task.

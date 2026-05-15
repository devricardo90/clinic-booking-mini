# Domain Model

Project: Clinic Booking Mini

Task: CBM-001

State: Local DONE

## Overview

The MVP domain is administrative booking for a fictitious aesthetic/dental clinic scenario.

The core entities are:

- Client
- Service
- Professional
- Appointment

No clinical records are part of the domain model.

## Client

Purpose: represents a fictitious person who may book an appointment.

Candidate administrative fields:

- id
- display_name
- phone
- email
- active
- created_at
- updated_at

Excluded fields:

- Diagnosis
- Clinical notes
- Medical history
- Anamnesis
- Prescriptions
- Treatment records
- Imaging or medical documents

## Service

Purpose: represents an appointment service that can be scheduled.

Candidate administrative fields:

- id
- name
- description
- duration_minutes
- active
- created_at
- updated_at

Example records:

- Initial evaluation
- Dental cleaning
- Whitening consultation
- Facial harmonization consultation
- Botox consultation

## Professional

Purpose: represents a fictitious professional available for appointments.

Candidate administrative fields:

- id
- display_name
- role_label
- active
- created_at
- updated_at

Excluded fields:

- Credential verification workflow
- Payroll data
- Sensitive HR data
- Clinical notes

## Appointment

Purpose: represents a scheduled administrative appointment.

Candidate administrative fields:

- id
- client
- service
- professional
- appointment_date
- start_time
- status
- created_at
- updated_at

Allowed statuses:

- SCHEDULED
- COMPLETED
- CANCELED
- NO_SHOW

Excluded fields:

- Diagnosis
- Prescription
- Treatment notes
- Clinical outcome
- Medical attachments
- Sensitive health information

## Relationships

- One Client can have many Appointments.
- One Service can be used by many Appointments.
- One Professional can have many Appointments.
- One Appointment belongs to exactly one Client, one Service, and one Professional.

## Status Meaning

- SCHEDULED: appointment is booked and expected to happen.
- COMPLETED: appointment was administratively completed.
- CANCELED: appointment was canceled and remains visible for context.
- NO_SHOW: client did not attend the scheduled appointment.

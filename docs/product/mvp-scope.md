# MVP Scope

Project: Clinic Booking Mini

Task: CBM-001

State: Local DONE

## Discussion Gate

### 1. What is the objective?

Define the MVP scope for a small Python/Django web app used by clinic administration staff to manage fictitious clients, services, professionals, appointment scheduling, appointment cancellation, daily appointment lists, and appointment status.

### 2. What does this add to the project?

It creates the first shared product baseline for the pilot. It documents what the MVP should include, what must remain out of scope, and which operational workflows should guide later implementation.

### 3. Where do we want to go?

The project should become a simple local administrative booking system for an aesthetic/dental clinic scenario. The first implementation target is a Django app using SQLite, Django templates, and basic CSS.

### 4. Why now?

CBM-001 is the first real pilot task for the official RIC Local Orchestrator runtime. A documented MVP boundary is needed before implementation begins so later tasks do not accidentally expand into medical records, integrations, payments, or production concerns.

### 5. What problem does it solve?

It solves the planning problem of coordinating a small clinic agenda without mixing administrative scheduling with clinical care records. The MVP focuses on who is booked, for which service, with which professional, at what time, and in which appointment status.

### 6. What is the minimum scope?

The minimum scope is documentation for:

- Client
- Service
- Professional
- Appointment
- Appointment statuses
- Basic administrative user flows
- MVP business rules
- Stack decision
- Operational status and backlog

No executable application code is part of CBM-001.

### 7. What are the risks?

- Scope creep into medical records or sensitive health data.
- Overbuilding features before confirming the administrative workflow.
- Ambiguous appointment status transitions.
- Confusing fictitious planning data with real client or health data.
- Adding infrastructure or dependencies before the MVP shape is approved.

### 8. What are the non-goals?

- Building a medical records system.
- Capturing diagnosis, prescription, treatment records, clinical notes, anamnesis, imaging, medical documents, real patient data, or sensitive health data.
- Installing Django or adding dependencies.
- Creating Python files, migrations, database schema, UI, Docker files, or a virtual environment.
- Adding authentication, payments, WhatsApp integration, or deployment.

### 9. How will we validate?

Validation for CBM-001 is a documentation review. The docs are valid when they clearly describe the MVP, respect the privacy/safety boundary, include the required entities and flows, and leave the project ready for a later implementation task only after explicit approval.

### 10. What is the DONE criterion?

CBM-001 reaches Local DONE when the documentation baseline has been reviewed and approved locally, all allowed documentation files are present, the scope and boundaries are clear, required evidence commands are run, and no code, dependency, push, or next task is started.

Local DONE is declared for CBM-001. Remote DONE is not declared.

## In Scope

- Fictitious client administration.
- Service catalog administration.
- Professional administration.
- Appointment creation.
- Appointment cancellation.
- Daily agenda view.
- Appointment status management.

## Out Of Scope

- Clinical documentation of any kind.
- Real patient or health data.
- Authentication and roles.
- Billing, invoicing, and payment collection.
- Messaging integrations.
- External frontend frameworks.
- Production deployment or hosting.

## MVP Appointment Statuses

- SCHEDULED
- COMPLETED
- CANCELED
- NO_SHOW

## Example Services

- Initial evaluation
- Dental cleaning
- Whitening consultation
- Facial harmonization consultation
- Botox consultation

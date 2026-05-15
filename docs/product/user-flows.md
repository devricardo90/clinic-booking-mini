# User Flows

Project: Clinic Booking Mini

Task: CBM-001

State: Local DONE

## Actor

The MVP actor is an administrative clinic user working with fictitious administrative data.

## Create Client

1. Open the client creation screen.
2. Enter fictitious administrative client details.
3. Save the client.
4. Confirm the client is available for appointment booking.

Validation notes:

- Do not collect medical history, diagnosis, clinical notes, or documents.
- Do not use real personal data.

## Create Service

1. Open the service creation screen.
2. Enter service name, optional administrative description, expected duration, and active state.
3. Save the service.
4. Confirm the service can be selected when creating an appointment.

Validation notes:

- Keep service information administrative.
- Do not document treatment outcomes or clinical protocols.

## Create Professional

1. Open the professional creation screen.
2. Enter fictitious professional display details.
3. Save the professional.
4. Confirm the professional can be selected when creating an appointment.

Validation notes:

- The MVP only needs scheduling identity.
- Licensing, credentialing, HR, and payroll workflows are out of scope.

## Create Appointment

1. Open the appointment creation screen.
2. Select a fictitious client.
3. Select a service.
4. Select a professional.
5. Select date and time.
6. Save the appointment.
7. Confirm the appointment appears with status SCHEDULED.

Validation notes:

- The appointment must not include clinical notes, diagnosis, prescription, or treatment records.

## View Daily Agenda

1. Open the daily agenda screen.
2. Select or confirm the target date.
3. Review appointments for that day.
4. Use status labels to identify scheduled, completed, canceled, and no-show appointments.

Expected fields:

- Appointment time
- Client display name
- Service
- Professional
- Status

## Cancel Appointment

1. Open an appointment from the agenda or appointment list.
2. Choose the cancel action.
3. Confirm cancellation.
4. Appointment status changes to CANCELED.
5. The appointment remains visible for administrative context.

Validation notes:

- Cancellation reason is optional and should remain administrative if added later.
- Do not record medical reasons or sensitive health data.

## Mark Appointment As Completed

1. Open a scheduled appointment.
2. Choose the complete action.
3. Confirm completion.
4. Appointment status changes to COMPLETED.

Validation notes:

- COMPLETED means the administrative appointment was attended or closed.
- It does not create or imply a treatment record.

## Mark Appointment As No-Show

1. Open a scheduled appointment.
2. Choose the no-show action.
3. Confirm no-show.
4. Appointment status changes to NO_SHOW.

Validation notes:

- NO_SHOW means the client did not attend.
- Do not record health-related explanations.

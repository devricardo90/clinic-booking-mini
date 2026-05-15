# Clinic Booking Mini Status

Project: Clinic Booking Mini

Runtime context: official RIC Local Orchestrator runtime, `ric-orchestrator-runtime:latest`

Current item: CBM-004

Current state: REVIEW

READY:

CBM-001 Remote DONE: declared at commit `4796bc9`

CBM-002 Remote DONE: declared at commit `20e91a3`

CBM-003 Remote DONE: declared at commit `425df38`

CBM-004 Local DONE: not declared

CBM-004 Remote DONE: not declared

## Summary

CBM-004 registers the existing scheduling models in Django Admin using simple `ModelAdmin` classes.

The registration covers `Client`, `Service`, `Professional`, and `Appointment` with `list_display`, `list_filter`, `search_fields`, `ordering`, and readonly `created_at` / `updated_at` fields.

No models, migrations, CRUD views, forms, URLs, templates, authentication changes, APIs, dependencies, deployment files, seed data, real data, or sensitive health data are included.

## Privacy And Safety Boundary

Clinic Booking Mini is not a medical records system.

The MVP must not include diagnosis, prescription, treatment records, clinical notes, anamnesis, imaging, medical documents, real patient data, or sensitive health data.

Only fictitious administrative data is allowed for local MVP testing.

## Review Notes

CBM-004 should be reviewed for:

- Django Admin registration only.
- No changes to `scheduling/models.py`.
- No migrations generated.
- No changes to settings, URLs, templates, views, forms, APIs, auth, dependencies, deployment, or seed data.
- Django check passing.
- No commit or push.

CBM-005 remains not opened.

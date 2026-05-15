# Stack Decision

Project: Clinic Booking Mini

Task: CBM-001

State: Local DONE

## Decision

The proposed MVP stack is:

- Python
- Django
- SQLite for local MVP persistence
- Django templates
- Basic CSS
- No external frontend framework for MVP

## Rationale

Django is a practical fit for a small administrative booking app because it supports conventional server-rendered CRUD workflows, simple relational models, and local development with SQLite.

SQLite is enough for the local MVP because the pilot is not a production deployment and does not require distributed storage.

Django templates and basic CSS are enough for the MVP because the required workflows are form and list based. An external frontend framework would increase setup cost without solving a current MVP problem.

## Constraints

CBM-001 is documentation-only. The stack is recorded for later implementation planning, but this task does not install Django, add dependencies, create Python files, create migrations, build UI, or configure runtime services.

## Deferred Decisions

- Project layout.
- Django app names.
- Model implementation details.
- Form validation details.
- Test strategy.
- Deployment strategy.
- Authentication and authorization.

## Non-Goals

- Docker setup.
- Virtual environment creation.
- Production hosting.
- External frontend build pipeline.
- Payment or messaging integrations.
- Medical records or sensitive health data handling.

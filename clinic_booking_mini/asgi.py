"""ASGI config for Clinic Booking Mini."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clinic_booking_mini.settings")

application = get_asgi_application()

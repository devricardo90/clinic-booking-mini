"""WSGI config for Clinic Booking Mini."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "clinic_booking_mini.settings")

application = get_wsgi_application()

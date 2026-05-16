"""URL configuration for the Clinic Booking Mini MVP foundation."""

from django.contrib import admin
from django.urls import path

from scheduling.views import appointment_new, appointment_success, home

urlpatterns = [
    path("", home, name="home"),
    path("appointments/new/", appointment_new, name="appointment_new"),
    path("appointments/success/", appointment_success, name="appointment_success"),
    path("admin/", admin.site.urls),
]

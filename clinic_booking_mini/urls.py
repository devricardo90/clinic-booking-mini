"""URL configuration for the Clinic Booking Mini MVP foundation."""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

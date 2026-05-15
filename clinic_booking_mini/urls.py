"""URL configuration for the Clinic Booking Mini MVP foundation."""

from django.contrib import admin
from django.urls import path

from scheduling.views import home

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
]

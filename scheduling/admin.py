from django.contrib import admin

from .models import Appointment, Client, Professional, Service


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("full_name", "phone", "email")
    ordering = ("full_name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "duration_minutes", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "role")
    search_fields = ("full_name", "role")
    ordering = ("full_name",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("client", "service", "professional", "scheduled_for", "status", "created_at", "updated_at")
    list_filter = ("status", "scheduled_for")
    search_fields = ("client__full_name", "service__name", "professional__full_name")
    ordering = ("scheduled_for",)
    readonly_fields = ("created_at", "updated_at")

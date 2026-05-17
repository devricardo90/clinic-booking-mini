from django.contrib import admin

from .forms import has_scheduling_conflict
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
    list_display = (
        "status",
        "scheduled_for",
        "client",
        "service",
        "professional",
        "client_phone",
        "client_email",
        "created_at",
    )
    list_display_links = ("scheduled_for",)
    list_filter = ("status", "service", "professional", "scheduled_for")
    search_fields = (
        "client__full_name",
        "client__phone",
        "client__email",
        "service__name",
        "professional__full_name",
    )
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "scheduled_for"
    actions = ("confirm_pending", "reject_pending", "mark_scheduled", "mark_canceled")
    fieldsets = (
        (
            "Appointment request",
            {
                "fields": (
                    "client",
                    "service",
                    "professional",
                    "scheduled_for",
                    "status",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": ("created_at", "updated_at"),
            },
        ),
    )

    @admin.display(description="Phone")
    def client_phone(self, obj):
        return obj.client.phone

    @admin.display(description="Email")
    def client_email(self, obj):
        return obj.client.email

    @admin.action(description="Confirm selected pending requests (PENDING → SCHEDULED)")
    def confirm_pending(self, request, queryset):
        non_pending = queryset.exclude(status=Appointment.Status.PENDING)
        if non_pending.exists():
            self.message_user(
                request,
                f"{non_pending.count()} appointment(s) skipped: only PENDING appointments can be confirmed.",
                level="warning",
            )
        confirmed = 0
        conflicted = 0
        for appt in queryset.filter(status=Appointment.Status.PENDING).select_related("service", "professional"):
            if has_scheduling_conflict(appt.professional, appt.scheduled_for, appt.service):
                conflicted += 1
            else:
                appt.status = Appointment.Status.SCHEDULED
                appt.save()
                confirmed += 1
        if confirmed:
            self.message_user(request, f"{confirmed} appointment request(s) confirmed as scheduled.")
        if conflicted:
            self.message_user(
                request,
                f"{conflicted} appointment request(s) could not be confirmed: scheduling conflict detected.",
                level="warning",
            )

    @admin.action(description="Reject selected pending requests (PENDING → REJECTED)")
    def reject_pending(self, request, queryset):
        non_pending = queryset.exclude(status=Appointment.Status.PENDING)
        if non_pending.exists():
            self.message_user(
                request,
                f"{non_pending.count()} appointment(s) skipped: only PENDING appointments can be rejected.",
                level="warning",
            )
        updated = queryset.filter(status=Appointment.Status.PENDING).update(
            status=Appointment.Status.REJECTED
        )
        if updated:
            self.message_user(request, f"{updated} appointment request(s) rejected.")

    @admin.action(description="Mark selected appointments as scheduled")
    def mark_scheduled(self, request, queryset):
        updated = queryset.update(status=Appointment.Status.SCHEDULED)
        self.message_user(request, f"{updated} appointment request(s) marked as scheduled.")

    @admin.action(description="Mark selected appointments as canceled")
    def mark_canceled(self, request, queryset):
        updated = queryset.update(status=Appointment.Status.CANCELED)
        self.message_user(request, f"{updated} appointment request(s) marked as canceled.")

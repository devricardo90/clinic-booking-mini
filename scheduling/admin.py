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
    list_display = (
        "scheduled_for",
        "status",
        "client",
        "client_phone",
        "client_email",
        "service",
        "professional",
        "created_at",
    )
    list_filter = ("status", "scheduled_for", "service", "professional")
    search_fields = (
        "client__full_name",
        "client__phone",
        "client__email",
        "service__name",
        "professional__full_name",
    )
    ordering = ("scheduled_for", "created_at")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "scheduled_for"
    actions = ("mark_scheduled", "mark_canceled")
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

    @admin.action(description="Mark selected appointments as scheduled")
    def mark_scheduled(self, request, queryset):
        updated = queryset.update(status=Appointment.Status.SCHEDULED)
        self.message_user(request, f"{updated} appointment request(s) marked as scheduled.")

    @admin.action(description="Mark selected appointments as canceled")
    def mark_canceled(self, request, queryset):
        updated = queryset.update(status=Appointment.Status.CANCELED)
        self.message_user(request, f"{updated} appointment request(s) marked as canceled.")

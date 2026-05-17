from datetime import time
from datetime import timedelta

from django import forms
from django.utils import timezone

from .models import Appointment, Professional, Service

OPENING_TIME = time(8, 0)
CLOSING_TIME = time(18, 0)


def has_scheduling_conflict(professional, scheduled_for, service):
    """Return True if scheduled_for overlaps any SCHEDULED appointment for the professional."""
    new_start = scheduled_for
    new_end = scheduled_for + timedelta(minutes=service.duration_minutes)
    candidates = (
        Appointment.objects.filter(
            professional=professional,
            status=Appointment.Status.SCHEDULED,
            scheduled_for__lt=new_end,
            scheduled_for__gte=new_start - timedelta(hours=8),
        )
        .select_related("service")
    )
    for appt in candidates:
        appt_end = appt.scheduled_for + timedelta(minutes=appt.service.duration_minutes)
        if appt_end > new_start:
            return True
    return False


class AppointmentRequestForm(forms.Form):
    full_name = forms.CharField(max_length=120, label="Full name")
    phone = forms.CharField(max_length=30, required=False, label="Phone")
    email = forms.EmailField(label="Email")
    service = forms.ModelChoiceField(
        queryset=Service.objects.none(),
        label="Service",
        empty_label="Select a service",
    )
    professional = forms.ModelChoiceField(
        queryset=Professional.objects.none(),
        label="Professional",
        empty_label="Select a professional",
    )
    scheduled_for = forms.DateTimeField(
        label="Preferred date and time",
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].queryset = Service.objects.filter(is_active=True).order_by("name")
        self.fields["professional"].queryset = Professional.objects.filter(is_active=True).order_by("full_name")

    def clean(self):
        cleaned_data = super().clean()
        service = cleaned_data.get("service")
        professional = cleaned_data.get("professional")
        scheduled_for = cleaned_data.get("scheduled_for")
        errors = []

        if scheduled_for:
            local_start = timezone.localtime(scheduled_for)

            if scheduled_for < timezone.now():
                errors.append("Appointments cannot be scheduled in the past.")

            if local_start.weekday() >= 5:
                errors.append("Appointments can only be scheduled Monday through Friday.")

            if local_start.time() < OPENING_TIME:
                errors.append("Appointments cannot start before 08:00.")

            if service:
                local_end = local_start + timedelta(minutes=service.duration_minutes)
                if local_end.date() != local_start.date() or local_end.time() > CLOSING_TIME:
                    errors.append("Appointments must finish by 18:00.")

        if professional and scheduled_for and service:
            if has_scheduling_conflict(professional, scheduled_for, service):
                errors.append(
                    "This time slot conflicts with an existing appointment for this professional."
                )

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data

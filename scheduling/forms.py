from django import forms

from .models import Professional, Service


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

from django.shortcuts import render

from .models import Appointment, Professional, Service


def home(request):
    services = Service.objects.filter(is_active=True).order_by("name")[:6]
    professionals = Professional.objects.filter(is_active=True).order_by("full_name")[:6]
    appointments = (
        Appointment.objects.select_related("client", "service", "professional")
        .filter(status=Appointment.Status.SCHEDULED)
        .order_by("scheduled_for")[:6]
    )

    return render(
        request,
        "scheduling/home.html",
        {
            "services": services,
            "professionals": professionals,
            "appointments": appointments,
        },
    )

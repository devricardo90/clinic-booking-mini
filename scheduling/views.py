from django.shortcuts import render
from django.shortcuts import redirect

from .forms import AppointmentRequestForm
from .models import Appointment, Client, Professional, Service


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


def appointment_new(request):
    if request.method == "POST":
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            client = Client.objects.filter(email=email).order_by("id").first()
            if client is None:
                client = Client(email=email)

            client.full_name = form.cleaned_data["full_name"]
            client.phone = form.cleaned_data["phone"]
            client.is_active = True
            client.save()

            Appointment.objects.create(
                client=client,
                service=form.cleaned_data["service"],
                professional=form.cleaned_data["professional"],
                scheduled_for=form.cleaned_data["scheduled_for"],
                status=Appointment.Status.SCHEDULED,
            )
            return redirect("appointment_success")
    else:
        form = AppointmentRequestForm()

    return render(request, "scheduling/appointment_form.html", {"form": form})


def appointment_success(request):
    return render(request, "scheduling/appointment_success.html")

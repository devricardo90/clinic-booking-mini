from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from scheduling.models import Appointment, Client, Professional, Service


class Command(BaseCommand):
    help = "Create or update fictitious demo data for local Clinic Booking Mini validation."

    def handle(self, *args, **options):
        services = [
            {"name": "Initial evaluation", "duration_minutes": 45, "is_active": True},
            {"name": "Dental cleaning", "duration_minutes": 60, "is_active": True},
        ]
        professionals = [
            {"full_name": "Dr. Ana Silva", "role": "Dentist", "is_active": True},
            {"full_name": "Dr. Bruno Costa", "role": "Aesthetic Specialist", "is_active": True},
        ]
        clients = [
            {
                "full_name": "Demo Client One",
                "phone": "+1 555 0101",
                "email": "demo.client.one@example.com",
                "is_active": True,
            },
            {
                "full_name": "Demo Client Two",
                "phone": "+1 555 0102",
                "email": "demo.client.two@example.com",
                "is_active": True,
            },
        ]

        service_objects = {}
        for service_data in services:
            service, _created = Service.objects.update_or_create(
                name=service_data["name"],
                defaults={
                    "duration_minutes": service_data["duration_minutes"],
                    "is_active": service_data["is_active"],
                },
            )
            service_objects[service.name] = service

        professional_objects = {}
        for professional_data in professionals:
            professional, _created = Professional.objects.update_or_create(
                full_name=professional_data["full_name"],
                defaults={
                    "role": professional_data["role"],
                    "is_active": professional_data["is_active"],
                },
            )
            professional_objects[professional.full_name] = professional

        client_objects = {}
        for client_data in clients:
            client, _created = Client.objects.update_or_create(
                email=client_data["email"],
                defaults={
                    "full_name": client_data["full_name"],
                    "phone": client_data["phone"],
                    "is_active": client_data["is_active"],
                },
            )
            client_objects[client.email] = client

        tz = timezone.get_current_timezone()
        appointment_data = [
            {
                "client": client_objects["demo.client.one@example.com"],
                "service": service_objects["Initial evaluation"],
                "professional": professional_objects["Dr. Ana Silva"],
                "scheduled_for": timezone.make_aware(datetime(2030, 1, 15, 9, 0), tz),
                "status": Appointment.Status.SCHEDULED,
            },
            {
                "client": client_objects["demo.client.two@example.com"],
                "service": service_objects["Dental cleaning"],
                "professional": professional_objects["Dr. Bruno Costa"],
                "scheduled_for": timezone.make_aware(datetime(2030, 1, 15, 10, 30), tz),
                "status": Appointment.Status.SCHEDULED,
            },
        ]

        for item in appointment_data:
            Appointment.objects.update_or_create(
                client=item["client"],
                service=item["service"],
                professional=item["professional"],
                scheduled_for=item["scheduled_for"],
                defaults={"status": item["status"]},
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Demo data ready: "
                f"{len(service_objects)} services, "
                f"{len(professional_objects)} professionals, "
                f"{len(client_objects)} clients, "
                f"{len(appointment_data)} appointments."
            )
        )

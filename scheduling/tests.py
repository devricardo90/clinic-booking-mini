from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Appointment, Client, Professional, Service


class PublicAppointmentRequestTests(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name="Initial evaluation", duration_minutes=45)
        self.professional = Professional.objects.create(full_name="Dr. Ana Silva", role="Dentist")
        self.client_record = Client.objects.create(
            full_name="Existing Client",
            phone="+1 555 0000",
            email="existing@example.com",
        )
        self.scheduled_for = timezone.make_aware(datetime(2030, 3, 1, 9, 0))
        Appointment.objects.create(
            client=self.client_record,
            service=self.service,
            professional=self.professional,
            scheduled_for=self.scheduled_for,
            status=Appointment.Status.SCHEDULED,
        )

    def _post_data(self, scheduled_for):
        return {
            "full_name": "Public Request Client",
            "phone": "+1 555 0909",
            "email": "public.request@example.com",
            "service": str(self.service.id),
            "professional": str(self.professional.id),
            "scheduled_for": scheduled_for.strftime("%Y-%m-%dT%H:%M"),
        }

    def test_public_request_blocks_same_professional_same_datetime(self):
        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(self.scheduled_for),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "This professional already has an appointment at the selected date and time.",
        )
        self.assertEqual(Appointment.objects.count(), 1)

    def test_public_request_allows_same_professional_different_datetime(self):
        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(self.scheduled_for + timedelta(hours=1)),
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("appointment_success"))
        self.assertEqual(Appointment.objects.count(), 2)

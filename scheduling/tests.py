from datetime import datetime, timedelta
from unittest.mock import Mock

from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .admin import AppointmentAdmin
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

    def test_public_request_blocks_past_datetime(self):
        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(timezone.now() - timedelta(days=1)),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Appointments cannot be scheduled in the past.")
        self.assertEqual(Appointment.objects.count(), 1)

    def test_public_request_blocks_weekend(self):
        saturday = timezone.make_aware(datetime(2030, 3, 2, 9, 0))

        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(saturday),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Appointments can only be scheduled Monday through Friday.")
        self.assertEqual(Appointment.objects.count(), 1)

    def test_public_request_blocks_before_opening_time(self):
        before_opening = timezone.make_aware(datetime(2030, 3, 4, 7, 30))

        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(before_opening),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Appointments cannot start before 08:00.")
        self.assertEqual(Appointment.objects.count(), 1)

    def test_public_request_blocks_when_service_ends_after_closing_time(self):
        late_start = timezone.make_aware(datetime(2030, 3, 4, 17, 30))

        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(late_start),
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Appointments must finish by 18:00.")
        self.assertEqual(Appointment.objects.count(), 1)

    def test_public_request_allows_same_professional_different_datetime(self):
        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(self.scheduled_for + timedelta(hours=1)),
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], reverse("appointment_success"))
        self.assertEqual(Appointment.objects.count(), 2)

    def test_success_page_shows_created_request_summary(self):
        response = self.client.post(
            reverse("appointment_new"),
            data=self._post_data(self.scheduled_for + timedelta(hours=2)),
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Appointment Request Received")
        self.assertContains(response, "Public Request Client")
        self.assertContains(response, "Initial evaluation")
        self.assertContains(response, "Dr. Ana Silva")
        self.assertContains(response, "Scheduled")


class AppointmentAdminLifecycleTests(TestCase):
    def setUp(self):
        self.service = Service.objects.create(name="Initial evaluation", duration_minutes=45)
        self.professional = Professional.objects.create(full_name="Dr. Ana Silva", role="Dentist")
        self.client_record = Client.objects.create(
            full_name="Admin Review Client",
            phone="+1 555 0100",
            email="admin.review@example.com",
        )
        self.appointment = Appointment.objects.create(
            client=self.client_record,
            service=self.service,
            professional=self.professional,
            scheduled_for=timezone.make_aware(datetime(2030, 3, 4, 9, 0)),
            status=Appointment.Status.SCHEDULED,
        )
        self.admin = AppointmentAdmin(Appointment, AdminSite())
        self.admin.message_user = Mock()
        self.request = Mock()

    def test_admin_can_mark_appointment_request_canceled(self):
        self.admin.mark_canceled(self.request, Appointment.objects.filter(id=self.appointment.id))

        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, Appointment.Status.CANCELED)
        self.admin.message_user.assert_called_once()

    def test_admin_can_mark_appointment_request_scheduled(self):
        self.appointment.status = Appointment.Status.CANCELED
        self.appointment.save()

        self.admin.mark_scheduled(self.request, Appointment.objects.filter(id=self.appointment.id))

        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, Appointment.Status.SCHEDULED)
        self.admin.message_user.assert_called_once()

from django.test import TestCase, Client
from django.urls import reverse
from .models import Team


class TeamModelTestCase(TestCase):

    def setUp(self):
        self.team = Team.objects.create(name="Test Team")

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertTrue(isinstance(self.team, Team))

    def test_team_str_method(self):
        self.assertEqual(str(self.team), "Test Team")


class TeamViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.team = Team.objects.create(name="Test Team")

    def test_team_list_view(self):
        url = reverse("team-list")  # Replace with actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.team.name)

    def test_team_detail_view(self):
        url = reverse(
            "team-detail", args=[self.team.id]
        )  # Replace with actual URL name and args
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.team.name)

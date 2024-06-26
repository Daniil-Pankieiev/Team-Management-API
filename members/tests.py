from django.test import TestCase, Client
from django.urls import reverse
from .models import Person
from teams.models import Team


class PersonModelTestCase(TestCase):

    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.person = Person.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            team=self.team,
        )

    def test_person_creation(self):
        self.assertEqual(self.person.first_name, "John")
        self.assertEqual(self.person.last_name, "Doe")
        self.assertEqual(self.person.email, "john.doe@example.com")
        self.assertEqual(self.person.team, self.team)
        self.assertTrue(isinstance(self.person, Person))

    def test_person_str_method(self):
        self.assertEqual(str(self.person), "John Doe")


class PersonViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.team = Team.objects.create(name="Test Team")
        self.person = Person.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            team=self.team,
        )

    def test_person_list_view(self):
        url = reverse("person-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.first_name)
        self.assertContains(response, self.person.last_name)

    def test_person_detail_view(self):
        url = reverse("person-detail", args=[self.person.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.first_name)
        self.assertContains(response, self.person.last_name)

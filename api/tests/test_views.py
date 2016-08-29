from django.urls import reverse
from django.test import TestCase, Client

from realty import factories
from api import serializers


class ProvincesTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_listing(self):
        url = reverse('province-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_listing_must_have_province(self):
        prov = factories.ProvinceFactory()
        url = reverse('province-list')

        response = self.client.get(url)

        serializer = serializers.ProvinceSerializer(prov)

        self.assertIn(serializer.data, response.data)


class PropertiesTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_listing(self):
        prop = factories.PropertyFactory()
        url = reverse('property-list')

        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)

        serializer = serializers.PropertySerializer(prop)
        self.assertIn(serializer.data, response.data['results'])

    def test_listing_with_search(self):
        prop_north = factories.PropertyFactory(x=1, y=10)
        prop_soulth = factories.PropertyFactory(x=1, y=1)

        url = reverse('property-list') + '?ax=0&ay=5&bx=2&by=0'

        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)

        serializer = serializers.PropertySerializer(prop_soulth)
        self.assertIn(serializer.data, response.data['results'])

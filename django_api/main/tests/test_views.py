import json

from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework import status

from main.models import Person


class TestPersonView(TestCase):

    def test_create_no_request_data(self):
        response = self.client.post(
            reverse('person'),
            content_type='application/json',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_create_ok(self):
        response = self.client.post(
            reverse('person'),
            json.dumps({'name': 'Alex'}),
            content_type='application/json',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.data[0]['name'],
            'Alex'
        )

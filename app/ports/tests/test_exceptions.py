import os

from django.test import TestCase, Client
from django.urls import reverse

from ports.models import Port
from MacPorts.config import TEST_PORTINDEX_JSON


class TestExceptions(TestCase):
    def setUp(self):
        self.client = Client()

    @classmethod
    def setUpTestData(cls):
        Port.load(TEST_PORTINDEX_JSON)

    def test_400(self):
        response = self.client.get('/testingA404')

        self.assertEquals(response.status_code, 404)
        self.assertTemplateUsed(response, template_name='404.html')

    def test_port_not_found(self):
        response = self.client.get(reverse('port_detail', kwargs={
            'name': 'testingA404.'
        }))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='ports/exceptions/port_not_found.html')

    def test_category_not_found(self):
        response = self.client.get(reverse('category_list', kwargs={
            'cat': 'thisCategoryshouldRaiseError'
        }))

        self.assertTemplateUsed(response, template_name='ports/exceptions/category_not_found.html')
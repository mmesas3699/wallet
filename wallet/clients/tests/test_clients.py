"""Tests for Clients."""

# Rest Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from wallet.clients.models import Client


class ClientsTests(APITestCase):

	def setUp(self):
		pass

	def test_request_success(self):
		url = "/api/clients/"
		response = self.client.get(url)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_client(self):
		url = "/api/clients/"
		data = {
			"document": "123456789",
			"names": "Pepe",
			"first_surname": "Perez",
			"second_surname": "Paez",
			"phone": "301234567",
			"address": "Calle 1 # 2 03",
			"email": "cualquier@cuenta.com",
		}
		response = self.client.post(url, data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_bad_request(self):
		"""Return bad request if data are invalid."""
		url = "/api/clients/"
		data = {
			"doc": "some"
		}
		response = self.client.post(url, data, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

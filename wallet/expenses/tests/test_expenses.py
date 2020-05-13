"""Tests for Expenses."""

# Rest Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from wallet.expenses.models import Expense


class ExpensesTests(APITestCase):

	def setUp(self):
		self.expense = Expense.objects.create(
			name="Enel",
			slug_name="enel",
			detail="Recibo de la Luz"
		)

	def test_list_expenses(self):
		url = "/api/expenses/"
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_expense(self):
		url = "/api/expenses/"
		data = {
			"name": "Agua",
			"slug_name": "agua",
			"detail": "Recibo del agua"
		}
		response = self.client.post(url, data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_bad_request_expense(self):
		url = "/api/expenses/"
		data = {
			"name": "Agua"
		}
		response = self.client.post(url, data, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

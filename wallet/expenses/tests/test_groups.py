"""Tests for Groups."""

# Rest Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from wallet.expenses.models import Group, Expense


class GroupTests(APITestCase):

	def setUp(self):
		self.group = Group.objects.create(
			name="Test",
			slug_name="test",
			detail="For testing purpose"
		)
		self.expense = Expense.objects.create(
			name="Gasto",
			slug_name="gasto",
			detail="Gasto de prueba",
		)
		
	def test_create_group(self):
		url = "/api/groups/"
		data = {
			"name": "Grupo",
			"slug_name": "grupo",
			"detail": "Grupo de prueba"
		}
		response = self.client.post(url, data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertIn("name", response.json())

	def test_add_expense_to_group(self):
		url = "/api/groups/{}/add_expenses/".format(self.group.slug_name)
		data = {"expenses": [self.expense.slug_name]}
		response = self.client.post(url, data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	# def test_remove_expense_from_group(self):
	# 	url = "/api/groups/{}/remove_expenses/".format(self.group.slug_name)
	# 	data = {"expense": self.expense.slug_name}
	# 	response = self.client.post(url, data, format="json")
	# 	self.assertEqual(response.status_code, status.HTTP_200_OK)

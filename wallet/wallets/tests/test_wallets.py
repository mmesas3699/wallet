"""Tests for Wallets."""

# Rest Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from wallet.wallets.models import Wallet

# Serializers
from wallet.wallets.serializers import WalletModelSerializer


class WalletTests(APITestCase):

    def setUp(self):
        self.wallet = Wallet.objects.create(
            name='davivienda',
            slug_name='davivienda',
            description='for test purpose',
            balance=10000,
        )

    def test_request_success(self):
        """Verify if requests is success."""

        response = self.client.get('/api/wallets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retreive_wallet(self):
        """Check if endpoint return wallet info."""

        url = "/api/wallets/{}/".format(self.wallet.slug_name)
        response = self.client.get(url)
        serializer = WalletModelSerializer(self.wallet)
        self.assertEqual(response.data, serializer.data)

    def test_income(self):
        """Checks if income process are executed correctly."""
        url = "/api/wallets/{}/income/".format(self.wallet.slug_name)
        data = {'amount': 10000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], 20000)

    def test_income_none_amount(self):
        """Checks if BadRequest is returned when no amount is sent."""
        url = "/api/wallets/{}/income/".format(self.wallet.slug_name)
        data = {'value': 1000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_income_negative_value(self):
        """Returns error if amount is less than one."""
        url = "/api/wallets/{}/income/".format(self.wallet.slug_name)
        data = {'amount': 0}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

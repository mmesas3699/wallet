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

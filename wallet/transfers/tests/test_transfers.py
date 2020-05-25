"""Test for Transfers."""

# Rest Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from wallet.transfers.models import Transfer
from wallet.wallets.models import Wallet

# Serializers
import wallet.transfers.serializers as transfer_serializers


class TransfersTests(APITestCase):

    def setUp(self):
        self.wallet_1 = Wallet.objects.create(
            name="davivienda",
            slug_name="davivienda",
            description="for test purpose",
            balance=10000)
        self.wallet_2 = Wallet.objects.create(
            name="billetera",
            slug_name="salario",
            description="for test purpose",
            balance=0)

    def test_make_transfer(self):
        url = "/api/transfers/"
        data = {
            "from_wallet": self.wallet_1.slug_name,
            "to_wallet": self.wallet_2.slug_name,
            "value": 500,
            "detail": "Testing"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 201)

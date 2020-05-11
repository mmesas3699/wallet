"""Wallet serializer."""

# Rest Framework

from rest_framework import serializers

# Models
from .models import Wallet


class WalletModelSerializer(serializers.ModelSerializer):
	"""Wallet model serializer."""

	class Meta:
		model = Wallet
		fields = '__all__'
		read_only_fields = ('balance',)


class WalletIncomeSerializer(serializers.ModelSerializer):
	"""For incomes to wallet."""

	amount = serializers.IntegerField(min_value=1)

	class Meta:
		model = Wallet
		fields = ['amount',]

	def update(self, instance, data):
		wallet = instance
		wallet.income(data['amount'])

		return wallet


class WalletWithdrawSerializer(serializers.ModelSerializer):
	"""For withdraw from wallets."""

	amount = serializers.IntegerField(min_value=1)

	class Meta:
		model = Wallet
		fields = ['amount',]

	def update(self, instance, data):
		"""If the amount is greater than balance return error."""
		wallet = instance
		try:
			wallet.withdraw(data['amount'])
		except Exception as error:
			raise error

		return wallet


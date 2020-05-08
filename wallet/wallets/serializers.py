"""Wallet serializer."""

# Rest Framework

from rest_framework.serializers import ModelSerializer

# Models
from .models import Wallet


class WalletModelSerializer(ModelSerializer):
	"""Wallet model serializer."""

	class Meta:
		model = Wallet
		fields = '__all__'
		read_only_fields = ('balance',)

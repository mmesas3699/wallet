# Rest Framework
from rest_framework import mixins, viewsets

# Models
from .models import Wallet

# Serializers
from .serializers import WalletModelSerializer


class WalletViewSet(mixins.RetrieveModelMixin,
					mixins.ListModelMixin,
					viewsets.GenericViewSet):
	"""Wallet viewset"""

	serializer_class = WalletModelSerializer
	queryset = Wallet.objects.all()
	lookup_field = 'slug_name'

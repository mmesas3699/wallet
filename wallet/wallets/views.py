# Rest Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

# Models
from .models import Wallet

# Serializers
from .serializers import WalletModelSerializer
from .serializers import WalletIncomeSerializer
from .serializers import WalletWithdrawSerializer


class WalletViewSet(mixins.RetrieveModelMixin,
					mixins.ListModelMixin,
					mixins.UpdateModelMixin,
					mixins.CreateModelMixin,
					viewsets.GenericViewSet):
	"""Wallet viewset"""

	serializer_class = WalletModelSerializer
	queryset = Wallet.objects.all()
	lookup_field = 'slug_name'

	def get_serializer_class(self):
		"""Return serializer based on action."""
		if self.action == 'income':
			return WalletIncomeSerializer
		elif self.action == 'withdraw':
			return WalletWithdrawSerializer

		return WalletModelSerializer

	@action(detail=True, methods=['post'])
	def income(self, request, pk=None, *args, **kargs):
		wallet = self.get_object()
		serializer_class = self.get_serializer_class()
		amount = request.data.get('amount')
		serializer = serializer_class(
			wallet,
			data={'amount': amount},
			partial=True
		)
		serializer.is_valid(raise_exception=True)
		wallet = serializer.save()
		data = WalletModelSerializer(wallet).data
		
		return Response(data, status=status.HTTP_200_OK)

	@action(detail=True, methods=['post'])
	def withdraw(self, request, pk=None, *args, **kwargs):
		wallet = self.get_object()
		serializer_class = self.get_serializer_class()
		amount = request.data.get('amount')
		serializer = serializer_class(
			wallet,
			data={'amount': amount},
			partial=True
		)
		serializer.is_valid(raise_exception=True)
		wallet = serializer.save()
		data = WalletModelSerializer(wallet).data

		return Response(data, status=status.HTTP_200_OK)
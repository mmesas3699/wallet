"""Transfer view."""

# Rest Framework
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

# Django
from django.shortcuts import get_object_or_404

# Serializers
from wallet.transfers.serializers import (TransferModelSerializer,
    MakeTransferSerializer)

# Models
from wallet.transfers.models import Transfer
from wallet.wallets.models import Wallet


class TransferViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      viewsets.GenericViewSet):

    queryset = Transfer.objects.all()
    
    def get_serializer_class(self):
        if self.action == "create":
            return MakeTransferSerializer

        return TransferModelSerializer

    def create(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data,)
        serializer.is_valid(raise_exception=True)
        transfer = serializer.save()
        data = TransferModelSerializer(transfer).data

        return Response(data, status=status.HTTP_201_CREATED)

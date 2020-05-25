"""Payment views."""

# Rest Framework
from rest_framework import mixins, viewsets

# Models
from wallet.payments.models import Payment

# Serializers
from wallet.payments.serializers import PaymentModelSerializer


class PaymentViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentModelSerializer

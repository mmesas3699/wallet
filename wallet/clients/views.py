# Rest Framework
from rest_framework import mixins, viewsets

# Models
from wallet.clients.models import Client

# Serializers
from wallet.clients.serializers import ClientModelSerializer


class ClientViewSet(mixins.ListModelMixin,
					mixins.UpdateModelMixin,
					mixins.RetrieveModelMixin,
					mixins.CreateModelMixin,
					viewsets.GenericViewSet):

	queryset = Client.objects.all()
	serializer_class = ClientModelSerializer

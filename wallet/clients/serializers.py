# Rest Framework
from rest_framework import serializers

# Models
from wallet.clients.models import Client


class ClientModelSerializer(serializers.ModelSerializer):

	class Meta:
		model = Client
		fields = "__all__"
		read_only_field = ["document",]

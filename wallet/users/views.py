# Rest Framework
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

# Models
from wallet.users.models import User

# Serializers
from wallet.users.serializers import UserModelSerializer


class UserViewSet(mixins.ListModelMixin, 
				  mixins.RetrieveModelMixin,
				  GenericViewSet):
	
	queryset = User.objects.all()
	serializer_class = UserModelSerializer

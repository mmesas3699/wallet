# Rest Framework
from rest_framework.serializers import ModelSerializer

# Models
from wallet.users.models import User


class UserModelSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

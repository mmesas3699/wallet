"""Group serializers."""

# Rest Framework
from rest_framework import serializers

# Models
from wallet.expenses.models import Group

# Serializers
from wallet.expenses.serializers import ExpenseModelSerializer


class GroupModelSerializer(serializers.ModelSerializer):

	expenses = ExpenseModelSerializer(many=True)

	class Meta
		model = Group
		fields = ('name', 'slug_name', 'detail')




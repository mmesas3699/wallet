"""Expense serializers."""

# Rest Framework
from rest_framework import serializers

# Models
from wallet.expenses.models import Expense


class ExpenseModelSerializer(serializers.ModelSerializer):
	
	groups = serializers.StringRelatedField(many=True, read_only=True)

	class Meta:
		model = Expense
		fields = ('name', 'slug_name', 'detail', 'groups')

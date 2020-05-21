"""Group serializers."""

# Rest Framework
from rest_framework import serializers

# Models
from wallet.expenses.models import Expense, Group

# Serializers
from wallet.expenses.serializers import ExpenseModelSerializer


class GroupModelSerializer(serializers.ModelSerializer):

	# expenses = ExpenseModelSerializer(source="expense_set", many=True)
	expenses = serializers.SlugRelatedField(
		many=True,
		slug_field='slug_name',
		read_only=True,
		source='expense_set'
	)

	class Meta:
		model = Group
		fields = ('name', 'slug_name', 'detail', 'expenses')



class AddExpenseToGroupSerializer(serializers.Serializer):
	"""Handling the adding of expenses to groups.

	expenses must be a list.
	
	"""

	expenses = serializers.ListField(
		child=serializers.SlugField(), 
		allow_empty=False,
	)

	class Meta:
		model = Group

	def validate_expenses(self, value):
		"""Validate if all the expenses in value list exists."""

		data = value
		expenses = []
		missing = []

		for slug in data:
			expense = Expense.objects.filter(slug_name=slug)
			
			if expense.exists():
				expenses.append(expense[0])
				# print('expenses', expenses)
			else:
				missing.append(slug)
				# print('missing', missing)

		if missing:
			raise serializers.ValidationError(f"Los gastos: {missing} no existen.!!")

		return expenses

	def update(self, instance, validated_data):
		group = instance
		expenses = validated_data['expenses']

		for expense in expenses:
			expense.groups.add(group)

		return group


class RemoveExpenseFromGroupSerializer(serializers.Serializer):
	"""Remove expense from groups."""

	expense =  serializers.SlugField()

	def validate_expense(self, expense):
		group = self.context['group']
		query = group.expense_set.filter(slug_name=expense)
		print(query)
		if query.exists():
			return expense
		else:
			return serializers.ValidationError(f"{expense} no pertenece a este grupo")

	def update(self, instance, validated_data):
		group = instance
		expense = Expense.objects.get(slug_name=validated_data['expense'])
		group.expense_set.remove(expense)

		return group

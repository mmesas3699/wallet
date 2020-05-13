# Rest Framework
from rest_framework import mixins, viewsets

# Models
from wallet.expenses.models import Expense

# Serializers
from wallet.expenses.serializers import ExpenseModelSerializer


class ExpenseViewSet(mixins.ListModelMixin,
					 mixins.RetrieveModelMixin,
					 mixins.CreateModelMixin,
					 mixins.UpdateModelMixin,
					 viewsets.GenericViewSet):

	queryset = Expense.objects.all()
	serializer_class = ExpenseModelSerializer
	lookup_field = 'slug_name'

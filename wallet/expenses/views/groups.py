"""Group views."""

# Rest Framework
from rest_framework import (mixins, viewsets, status)
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from wallet.expenses.models import Group

# Serializers
from wallet.expenses.serializers import (
	AddExpenseToGroupSerializer,
	GroupModelSerializer,
	RemoveExpenseFromGroupSerializer,
)


class GroupViewSet(mixins.ListModelMixin,
				   mixins.CreateModelMixin,
				   mixins.RetrieveModelMixin,
				   mixins.UpdateModelMixin,
				   viewsets.GenericViewSet):
	"""Group view."""

	queryset = Group.objects.all()
	lookup_field = 'slug_name'

	def get_serializer_class(self):
		if self.action == "add_expenses":
			return AddExpenseToGroupSerializer
		elif self.action == "remove_expenses":
			return RemoveExpenseFromGroupSerializer

		return GroupModelSerializer

	@action(detail=True, methods=["post"])
	def add_expenses(self, request, *args, **kwargs):
		group = self.get_object()
		serializer_class = self.get_serializer_class()
		serializer = serializer_class(group, data=request.data)
		serializer.is_valid(raise_exception=True)
		group = serializer.save()
		data = GroupModelSerializer(group).data

		return Response(data, status=status.HTTP_201_CREATED)

	@action(detail=True, methods=["post"])
	def remove_expenses(self, request, *args, **kwargs):
		group = self.get_object()
		serializer_class = self.get_serializer_class()
		serializer = serializer_class(
			group,
			data=request.data,
			context= {
				"group": group
			}
		)
		serializer.is_valid(raise_exception=True)
		group = serializer.save()
		data = GroupModelSerializer(group).data

		return Response(data, status=status.HTTP_200_OK)

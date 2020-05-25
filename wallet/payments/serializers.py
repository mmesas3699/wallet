"""Payment serializers."""

# Rest Framework
from rest_framework import serializers

# Models
from wallet.expenses.models import Expense
from wallet.payments.models import Payment
from wallet.wallets.models import Wallet


class PaymentModelSerializer(serializers.ModelSerializer):

    expense = serializers.SlugRelatedField(
        slug_field="slug_name",
        queryset=Expense.objects.all())
    wallet = serializers.SlugRelatedField(
        slug_field="slug_name",
        queryset=Wallet.objects.all())

    class Meta:
        model = Payment
        fields = ["id", "date", "value", "expense", "wallet", "detail", "invoice"]

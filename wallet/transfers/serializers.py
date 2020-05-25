"""Transfer serializers."""

# Rest Framework
from rest_framework import serializers
from rest_framework.mixins import status
from rest_framework.exceptions import NotFound

# Django
from django.db import transaction

# Models
from wallet.transfers.models import Transfer
from wallet.wallets.models import Wallet


class TransferModelSerializer(serializers.ModelSerializer):
    from_wallet = serializers.SlugRelatedField(
        read_only=True,
        slug_field="slug_name")
    to_wallet = serializers.SlugRelatedField(
        read_only=True,
        slug_field="slug_name")
    
    class Meta:
        model = Transfer
        fields = ("id", "from_wallet", "to_wallet", "value", "detail", "date")
    

class MakeTransferSerializer(serializers.Serializer):
    """Serializer for make transfers.

    Checks if the balance of the wallet from which the transfer leaves
    has a sufficient ammount."""

    from_wallet = serializers.CharField()
    to_wallet = serializers.CharField()
    value = serializers.IntegerField(min_value=1)
    detail = serializers.CharField(max_length=200)

    def validate_from_wallet(self, value):
        """Validate if wallet exists."""
        query = Wallet.objects.filter(slug_name=value)

        if query.exists():
            value = query[0]
            return value
        
        error = {"error": f"No existe: {value}"}
        raise serializers.ValidationError(error)

    def validate_to_wallet(self, value):
        """Validate if wallet exists."""
        query = Wallet.objects.filter(slug_name=value)

        if query.exists():
            value = query[0]
            return value
        
        error = {"error": f"No existe: {value}"}
        raise serializers.ValidationError(error)

    def validate(self, data):
        """Checks if the balance of the Wallet from which the
        transfer leaves has a sufficient balance."""
        value = data["value"]
        from_wallet = data["from_wallet"]

        if value > from_wallet.balance:
            error = f"{from_wallet.slug_name} no tiene saldo suficiente."
            raise serializers.ValidationError(error)

        return data

    def create(self, validated_data):
        from_wallet = validated_data["from_wallet"]
        to_wallet = validated_data["to_wallet"]
        value = validated_data["value"]

        with transaction.atomic():
            # Update wallets balance
            from_wallet.withdraw(value)
            to_wallet.income(value)

            # Create transfer
            transfer = Transfer.objects.create(**validated_data)
        
        return transfer

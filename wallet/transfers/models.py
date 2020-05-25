"""Transfers models."""

# Django
from django.db import models

# Models
from wallet.wallets.models import Wallet


class Transfer(models.Model):
    from_wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="transfer_from"
    )
    to_wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="transfer_to"
    )
    value = models.PositiveIntegerField()
    detail = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self}"

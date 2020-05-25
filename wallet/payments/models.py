"""Payment models."""

# Django
from django.db import models

# Models
from wallet.expenses.models import Expense
from wallet.wallets.models import Wallet


class Payment(models.Model):
    expense = models.ForeignKey(
        Expense,
        on_delete=models.PROTECT,
        related_name="payments")
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="payments")
    value = models.PositiveIntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length=120)
    invoice = models.CharField(max_length=80)

    def save(self, *args, **kwargs):
        """For update de Wallet balance."""
        wallet = self.wallet.withdraw(self.value)
        super(Payment, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.date}, {self.expense}, value: {self.value}"

    class Meta:
        ordering = ["-date"]

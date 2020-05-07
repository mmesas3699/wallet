"""Wallet model."""

# Django
from django.db import models


class Wallet(models.Model):
	name = models.CharField(max_length=60, null=False, blank=False)
	slug_name = models.SlugField(
		help_text="Para el Banco de Bogotá: 'bogota' o 'bancobogota'", 
		unique=True
	)
	description = models.CharField(max_length=120)
	created = models.DateTimeField(auto_now_add=True)
	balance = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)

	def income(self, value):
		"""Increases the balance of the wallet."""
		
		self.balance += value
		self.save()  # save instance
		return self.balance

	def withdraw(self, value):
		"""Return an error if 'value' is bigger than the balance."""
		
		if value > self.balance:
			raise Exception("Saldo insuficiente")

		self.balance -= value
		self.save()  # save instance
		return self.balance

	def __str__(self):
		return f"{self.slug_name}: ${self.balance}"

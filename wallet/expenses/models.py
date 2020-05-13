# Django
from django.db import models


class Group(models.Model):
	"""To group expenses."""

	name = models.CharField(max_length=120)
	slug_name = models.SlugField(unique=True)
	detail = models.CharField(max_length=300)

	def __str__(self):
		return f"{self.slug_name}"


class Expense(models.Model):
	"""Expenses model."""

	name = models.CharField(max_length=160)
	slug_name = models.SlugField(unique=True)
	detail = models.CharField(max_length=300)
	groups = models.ManyToManyField(Group)

	def __str__(self):
		return f"{self.slug_name}"

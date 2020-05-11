# Django
from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
	
	# Validators
	document_regex = RegexValidator(
		regex=r'\d{1,12}$',
		message="Ingrese el número de documento sin caracteres especiales. Maximo once caracteres."
	)

	phone_regex = RegexValidator(
		regex=r'^\d{1,10}$',
		message="Maximo 10 caracteres."
	)

	# Fields
	document = models.CharField(
		primary_key=True,
		max_length=11,
		blank=False,
		null=False,
		validators=[document_regex]
	)
	names = models.CharField(max_length=120, blank=False, null=False)
	first_surname = models.CharField(max_length=120, blank=False, null=False)
	second_surname = models.CharField(max_length=120, blank=False, null=False)
	phone = models.CharField(
		max_length=10,
		blank=False,
		null=False,
		validators=[phone_regex]
	)
	address = models.CharField(max_length=180, blank=False, null=False)
	email = models.EmailField()

	def __str__(self):
		return f"{self.names} {self.first_surname}"

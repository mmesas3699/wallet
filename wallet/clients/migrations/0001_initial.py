# Generated by Django 3.0.5 on 2020-05-11 03:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('document', models.CharField(max_length=11, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Ingrese el número de documento sin caracteres especiales. Maximo once caracteres.', regex='^\\d{1,11}$')])),
                ('names', models.CharField(max_length=120)),
                ('first_surname', models.CharField(max_length=120)),
                ('second_surname', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Maximo 10 caracteres.', regex='^\\d{10}$')])),
                ('address', models.CharField(max_length=180)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

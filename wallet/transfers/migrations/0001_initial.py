# Generated by Django 3.0.5 on 2020-05-21 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
                ('detail', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now=True)),
                ('from_wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_from', to='wallets.Wallet')),
                ('to_wallet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_to', to='wallets.Wallet')),
            ],
        ),
    ]
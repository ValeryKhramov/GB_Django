# Generated by Django 5.0.3 on 2024-03-31 19:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number_phone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('registration_date', models.CharField(default=datetime.date(2024, 3, 31), max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('count_products', models.IntegerField()),
                ('date_added', models.CharField(default=datetime.date(2024, 3, 31), max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_of_registration', models.CharField(default=datetime.date(2024, 3, 31), max_length=12)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework2app.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework2app.product')),
            ],
        ),
    ]

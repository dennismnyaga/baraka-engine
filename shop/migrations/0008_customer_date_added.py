# Generated by Django 5.1.3 on 2024-11-21 11:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_orders_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
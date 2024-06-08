# Generated by Django 3.2.25 on 2024-06-08 14:09

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_auto_20240605_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='reminder_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 13, 15, 8, 46, 726990)),
        ),
    ]

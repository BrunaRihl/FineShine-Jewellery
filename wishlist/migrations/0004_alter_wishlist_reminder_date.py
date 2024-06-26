# Generated by Django 3.2.25 on 2024-06-08 15:43

from django.db import migrations, models
import wishlist.models


class Migration(migrations.Migration):

    dependencies = [
        ("wishlist", "0003_auto_20240608_1509"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="reminder_date",
            field=models.DateTimeField(
                default=wishlist.models.get_default_reminder_date
            ),
        ),
    ]

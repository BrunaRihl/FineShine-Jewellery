# Generated by Django 3.2.25 on 2024-04-30 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
# Generated by Django 3.2 on 2022-01-05 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_sub_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
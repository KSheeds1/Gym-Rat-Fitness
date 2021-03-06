# Generated by Django 3.2 on 2022-01-06 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_rating'),
        ('reviews', '0002_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.DecimalField(choices=[(1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], decimal_places=1, default=1.0, max_digits=3),
        ),
    ]

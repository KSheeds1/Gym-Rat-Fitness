# Generated by Django 3.2 on 2021-12-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211222_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]

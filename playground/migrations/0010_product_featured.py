# Generated by Django 5.1 on 2024-08-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0009_remove_product_featured"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(null=True),
        ),
    ]

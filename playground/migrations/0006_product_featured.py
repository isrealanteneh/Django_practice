# Generated by Django 5.1 on 2024-08-16 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0005_product_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]

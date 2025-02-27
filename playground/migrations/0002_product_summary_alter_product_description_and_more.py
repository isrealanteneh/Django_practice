# Generated by Django 5.1 on 2024-08-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playground", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="summary",
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name="product",
            name="title",
            field=models.CharField(max_length=120),
        ),
    ]

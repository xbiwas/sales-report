# Generated by Django 5.0.6 on 2024-05-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales", "0003_remove_sale_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="total_price",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
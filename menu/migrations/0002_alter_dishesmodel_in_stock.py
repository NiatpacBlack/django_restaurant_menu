# Generated by Django 4.1.4 on 2022-12-26 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dishesmodel",
            name="in_stock",
            field=models.BooleanField(default=True, verbose_name="В наличии"),
        ),
    ]

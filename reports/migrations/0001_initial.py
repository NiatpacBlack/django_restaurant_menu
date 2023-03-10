# Generated by Django 4.1.4 on 2022-12-27 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("menu", "0002_alter_dishesmodel_in_stock"),
    ]

    operations = [
        migrations.CreateModel(
            name="SelectionDishesModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "selection_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Время нажатия"
                    ),
                ),
                (
                    "dish",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="selection_dishes",
                        to="menu.dishesmodel",
                        verbose_name="Id товара",
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="selection_users",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Статистика товара",
                "verbose_name_plural": "Статистика товаров",
                "db_table": "selection_dishes",
            },
        ),
    ]

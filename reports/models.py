from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from menu.models import DishesModel


class SelectionDishesModel(models.Model):
    """Таблица, в которой хранятся данные о нажатии на определенное блюдо из меню."""

    username = models.ForeignKey(
        User,
        related_name="selection_users",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    dish = models.ForeignKey(
        DishesModel,
        related_name="selection_dishes",
        on_delete=models.CASCADE,
        verbose_name="id товара",
    )
    selection_time = models.DateTimeField(
        default=timezone.now, verbose_name="Время нажатия"
    )

    def __str__(self):
        return str(self.dish_id)

    class Meta:
        db_table = "selection_dishes"
        verbose_name = "Статистика выбора товара"
        verbose_name_plural = "Статистика выбора товаров"

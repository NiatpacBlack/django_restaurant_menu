from django.db import models


class MenuCategoriesModel(models.Model):
    """Таблица с категориями меню."""

    category_name = models.CharField(max_length=255, verbose_name="Категория")

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "menu_categories"
        verbose_name = "Категория меню"
        verbose_name_plural = "Категории меню"


class DishesModel(models.Model):
    """Таблица с блюдами."""

    dish_name = models.CharField(max_length=255, verbose_name="Название блюда")
    category = models.ForeignKey(
        MenuCategoriesModel,
        related_name="dishes",
        on_delete=models.CASCADE,
        verbose_name="Категория блюда",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="Описание")
    in_stock = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return self.dish_name

    class Meta:
        db_table = "dishes"
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

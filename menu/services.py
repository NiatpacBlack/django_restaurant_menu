from django.http import Http404
from django.db.models.query import QuerySet
from .models import MenuCategoriesModel, DishesModel


def get_all_categories_from_menu() -> QuerySet[MenuCategoriesModel]:
    """Возвращает QuerySet со всеми категориями из таблицы MenuCategoriesModel."""
    return MenuCategoriesModel.objects.all()


def get_all_dishes_from_menu() -> QuerySet[MenuCategoriesModel]:
    """Возвращает QuerySet со всеми блюдами из таблицы Dishes."""
    return DishesModel.objects.all()


def get_not_empty_category_id() -> list[int, ...] | list:
    """
    Возвращает список id категорий в которых есть блюда.

    Если все категории пустые, вернет пустой список.
    """
    queryset = DishesModel.objects.all()
    return list(set([el.category_id for el in queryset]))


def get_all_dishes_from_category_or_404(category_id: int) -> QuerySet[DishesModel]:
    """
    Возвращает QuerySet со всеми блюдами из отдельной категории id которой совпадает с id в таблице категорий.

    В случае отсутствия данных в QuerySet - возвращает ошибку 404.
    """
    queryset = DishesModel.objects.filter(category_id=category_id)
    if queryset:
        return queryset
    raise Http404("Категории с таким id не существует в меню.")


def get_dish_description_or_404(dish_id: int) -> QuerySet[DishesModel]:
    """
    Возвращает QuerySet со всеми данными о конкретном блюде id которого совпадает с id в таблице блюд.

    В случае отсутствия данных в QuerySet - возвращает ошибку 404.
    """
    queryset = DishesModel.objects.filter(id=dish_id)
    if queryset:
        return queryset
    raise Http404("Блюдо с таким id не существует в меню.")

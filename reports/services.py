from .models import SelectionDishesModel


def add_selection_in_selection_dishes_table(username: str, dish_id: int):
    """
    Добавляет данные о пользователе и блюде, которое пользователь выбрал для просмотра, в таблицу selection_dishes.
    """
    SelectionDishesModel.objects.create(username=username, dish_id=dish_id)

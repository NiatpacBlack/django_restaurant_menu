from datetime import date

from django.contrib.auth.models import User

from .models import SelectionDishesModel


def add_selection_in_selection_dishes_table(username: str, dish_id: int):
    """
    Добавляет данные о пользователе и блюде, которое пользователь выбрал для просмотра, в таблицу selection_dishes.
    """
    SelectionDishesModel.objects.create(username=username, dish_id=dish_id)


def get_top_dishes_data(data_from: str, data_to: str, limit: int) -> list[dict[str, str | int], ...]:
    """
    Возвращает список кортежей с данными типа (название, количество нажатий) о наиболее популярных блюдах.

    Данные о блюдах получаются в количестве limit блюд, в диапазоне дат от data_from до data_to.
    """
    raw_query = fr"""
        select dish_id as id, dish_name, count(dish_id) as selected_count  
        from selection_dishes join dishes on selection_dishes.dish_id = dishes.id
        where not selection_time >= '{data_to or date.today()} 23:59:59' and selection_time >= '{data_from or '2022-01-01'} 00:00:01'
        group by dish_id, dish_name
        order by selected_count desc 
        limit {limit}
        """

    queryset = SelectionDishesModel.objects.raw(raw_query)
    return [{"name": el.dish_name, "count": el.selected_count} for el in queryset]


def get_top_users_data(data_from: str, data_to: str, limit: int) -> list[dict[str, str | int], ...]:
    """
    Возвращает список кортежей с данными типа (имя пользователя, количество нажатий) о самых активных пользователях.

    Данные о пользователях получаются в количестве limit пользователей, в диапазоне дат от data_from до data_to.
    """

    raw_query = fr"""
        select username_id as id, auth_user.username, count(username_id) as selected_count  
        from selection_dishes join auth_user on selection_dishes.username_id = auth_user.id
        where not selection_time >= '{data_to or date.today()} 23:59:59' and selection_time >= '{data_from or '2022-01-01'} 00:00:01'
        group by username_id, auth_user.username
        order by selected_count desc 
        limit {limit}
        """
    queryset = User.objects.raw(raw_query)
    return [{"name": el.username, "count": el.selected_count} for el in queryset]

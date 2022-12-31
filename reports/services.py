import datetime
from datetime import date

from django.contrib.auth.models import User

from .models import SelectionDishesModel


def add_selection_in_selection_dishes_table(username: str, dish_id: int) -> None:
    """
    Добавляет данные о пользователе и блюде, которое пользователь выбрал для просмотра, в таблицу selection_dishes.
    """
    SelectionDishesModel.objects.create(username=username, dish_id=dish_id)


def get_top_dishes_data(
    data_from: str, data_to: str, limit: int
) -> list[dict[str, str], ...]:
    """
    Возвращает список кортежей с данными типа (название, количество нажатий) о наиболее популярных блюдах.

    Данные о блюдах получаются в количестве limit блюд, в диапазоне дат от data_from до data_to.
    """
    raw_query = rf"""
        select dish_id as id, dish_name, count(dish_id) as selected_count  
        from selection_dishes join dishes on selection_dishes.dish_id = dishes.id
        where not selection_time >= '{data_to or date.today()} 23:59:59' and selection_time >= '{data_from or '2022-01-01'} 00:00:01'
        group by dish_id, dish_name
        order by selected_count desc 
        limit {limit}
        """

    queryset = SelectionDishesModel.objects.raw(raw_query)
    return [{"name": el.dish_name, "count": el.selected_count} for el in queryset]


def get_top_users_data(
    data_from: str, data_to: str, limit: int
) -> list[dict[str, str], ...]:
    """
    Возвращает список кортежей с данными типа (имя пользователя, количество нажатий) о самых активных пользователях.

    Данные о пользователях получаются в количестве limit пользователей, в диапазоне дат от data_from до data_to.
    """

    raw_query = rf"""
        select username_id as id, auth_user.username, count(username_id) as selected_count  
        from selection_dishes join auth_user on selection_dishes.username_id = auth_user.id
        where not selection_time >= '{data_to or date.today()} 23:59:59' and selection_time >= '{data_from or '2022-01-01'} 00:00:01'
        group by username_id, auth_user.username
        order by selected_count desc 
        limit {limit}
        """
    queryset = User.objects.raw(raw_query)
    return [{"name": el.username, "count": el.selected_count} for el in queryset]


def get_top_users_from_category(
    data_from: str, data_to: str, category_id: str, limit: str
) -> list[dict[str, str, str], ...]:
    """
    Возвращает список кортежей с данными о самых активных пользователях в конкретной категории с id = category_id.

    Данные возвращаются в формате (имя пользователя, название категории, количество нажатий).
    Данные о пользователях получаются в количестве limit пользователей, в диапазоне дат от data_from до data_to.
    """

    raw_query = rf"""
        select au.id, au.username, mc.category_name, count(sd.username_id) as selected_count from selection_dishes sd
        join dishes d on d.id = sd.dish_id
        join auth_user au on au.id = sd.username_id
        join menu_categories mc on mc.id = d.category_id 
        where category_id = {category_id} and sd.selection_time >= '{data_from or '2022-01-01'} 00:00:01' and not sd.selection_time >= '{data_to or date.today()} 23:59:59'
        group by au.id, au.username, mc.category_name
        order by selected_count desc
        limit {limit}
        """
    queryset = User.objects.raw(raw_query)
    return [
        {"name": el.username, "category": el.category_name, "count": el.selected_count}
        for el in queryset
    ]


def get_dish_report_data(
    report_name: str, dish_id
) -> None | dict[str, str | list[str, ...] | list[int, ...]]:
    """Возвращает данные для построения графика для отчета report_name о нажатиях на блюдо c dish_id."""
    if report_name == "Отчет по дням недели":
        return {
            "report_title": "по дням недели",
            "x_axis": ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вскр"],
            "report_data": get_dish_report_data_by_week_days(dish_id=dish_id),
        }
    elif report_name == "Отчет по часам":
        return {
            "report_title": "по часам",
            "x_axis": [str(number) for number in range(24)],
            "report_data": get_dish_report_data_by_hours(dish_id=dish_id),
        }


def get_dish_report_data_by_week_days(dish_id: str) -> list[int, ...]:
    """Возвращает данные о нажатиях на блюдо с dish_id по каждому дню недели."""
    week_data_list = [0 for _ in range(7)]
    queryset = SelectionDishesModel.objects.filter(dish_id=dish_id)
    for el in queryset:
        week_data_list[datetime.datetime.weekday(el.selection_time)] += 1
    return week_data_list


def get_dish_report_data_by_hours(dish_id: str) -> list[int, ...]:
    """Возвращает данные о нажатиях на блюдо с dish_id по каждому конкретному часу в сутках."""
    hours_data_list = [0 for _ in range(24)]
    queryset = SelectionDishesModel.objects.filter(dish_id=dish_id)
    for el in queryset:
        hour = int(
            el.selection_time.astimezone(
                datetime.timezone(datetime.timedelta(hours=3))
            ).strftime("%H")
        )
        hours_data_list[hour] += 1
    return hours_data_list

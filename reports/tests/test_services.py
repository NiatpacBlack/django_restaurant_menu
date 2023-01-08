from datetime import date
from django.contrib.auth.models import User
from django.test import TestCase

from menu.models import MenuCategoriesModel, DishesModel
from ..models import SelectionDishesModel
from ..services import add_selection_in_selection_dishes_table, get_top_dishes_data, get_top_users_data, \
    get_top_users_from_category, get_dish_report_data, get_dish_report_data_by_week_days, get_dish_report_data_by_hours


class ReportsServicesTest(TestCase):
    """
    Тесты функций из файла reports.services.
    Для работы тестов в меню будут временно добавлены: Категория, Блюдо, Пользователь, Нажатие на блюдо пользователем.
    """

    def setUp(self) -> None:
        MenuCategoriesModel.objects.create(category_name="TestCategory9999")
        self.test_category = MenuCategoriesModel.objects.filter(category_name="TestCategory9999").first()

        DishesModel.objects.create(
            dish_name="TestDish9999",
            category_id=self.test_category.id,
            price=5.5,
            description="Тестовое описание" * 99,
        )
        self.test_dish = DishesModel.objects.filter(dish_name="TestDish9999").first()

        User.objects.create_user(username='TestUser9999', email='testuser9999@gmail.com', password='testuser9999')
        self.test_username = User.objects.all().first()

        SelectionDishesModel.objects.create(username=self.test_username, dish_id=self.test_dish.id)

        self.len_all_selected_dishes = len(SelectionDishesModel.objects.all())

    def test_add_selection_in_selection_dishes_table(self) -> None:
        add_selection_in_selection_dishes_table(username=self.test_username, dish_id=self.test_dish.id)
        self.assertEqual(len(SelectionDishesModel.objects.all()), self.len_all_selected_dishes + 1)

    def test_get_top_dishes_data(self) -> None:
        self.assertEqual(get_top_dishes_data(data_from='2022-01-01', data_to=str(date.today()), limit=1),
                         [{'name': 'TestDish9999', 'count': 1}])

    def test_get_top_users_data(self) -> None:
        self.assertEqual(get_top_users_data(data_from='2022-01-01', data_to=str(date.today()), limit=1),
                         [{'name': 'TestUser9999', 'count': 1}])

    def test_get_top_users_from_category(self):
        self.assertEqual(get_top_users_from_category(data_from='2022-01-01', data_to=str(date.today()),
                                                     category_id=self.test_category.id, limit=1),
                         [{'name': 'TestUser9999', 'category': 'TestCategory9999', 'count': 1}])

    def test_get_dish_report_data(self) -> None:
        self.assertEqual(type(get_dish_report_data(report_name="Отчет по дням недели", dish_id=self.test_dish.id)),
                         dict)
        self.assertEqual(type(get_dish_report_data(report_name="Отчет по часам", dish_id=self.test_dish.id)), dict)
        self.assertEqual(get_dish_report_data(report_name="Неправильное название", dish_id=self.test_dish.id), None)
        self.assertEqual(type(get_dish_report_data(report_name="Отчет по часам", dish_id=9999959996999999)), dict)

    def test_get_dish_report_data_by_week_days(self):
        self.assertEqual(type(get_dish_report_data_by_week_days(dish_id=self.test_dish.id)), list)
        self.assertEqual(len(get_dish_report_data_by_week_days(dish_id=self.test_dish.id)), 7)
        self.assertEqual(get_dish_report_data_by_week_days(dish_id='9999959996999999'), [0 for _ in range(7)])

    def test_get_dish_report_data_by_hours(self):
        self.assertEqual(type(get_dish_report_data_by_hours(dish_id=self.test_dish.id)), list)
        self.assertEqual(len(get_dish_report_data_by_hours(dish_id=self.test_dish.id)), 24)
        self.assertEqual(get_dish_report_data_by_hours(dish_id='9999959996999999'), [0 for _ in range(24)])

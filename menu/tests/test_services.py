from django.http import Http404
from django.test import TestCase
from django.db.models.query import QuerySet
from ..services import get_all_categories_from_menu, get_not_empty_category_id, get_all_dishes_from_category_or_404, \
    get_dish_description_or_404, get_all_dishes_from_menu
from ..models import DishesModel, MenuCategoriesModel


class MenuServicesTest(TestCase):
    """Тесты функций из файла menu.services. Для работы тестов в меню будут временно добавлены категория и блюдо."""

    def setUp(self) -> None:
        MenuCategoriesModel.objects.create(category_name="TestCategory999")
        self.test_category = MenuCategoriesModel.objects.filter(category_name="TestCategory999").first()
        DishesModel.objects.create(
            dish_name="TestDish999",
            category_id=self.test_category.id,
            price=4.5,
            description="Тестовое описание" * 100,
        )
        self.test_dish = DishesModel.objects.filter(dish_name="TestDish999").first()

    def test_get_all_categories_from_menu(self) -> None:
        self.assertEqual(type(get_all_categories_from_menu()), QuerySet)

    def test_get_all_dishes_from_menu(self) -> None:
        self.assertEqual(type(get_all_dishes_from_menu()), QuerySet)

    def test_get_not_empty_category_id(self) -> None:
        self.assertEqual(type(get_not_empty_category_id()), list)

    def test_get_all_dishes_from_category_or_404(self) -> None:
        self.assertEqual(type(get_all_dishes_from_category_or_404(category_id=self.test_category.id)), QuerySet)
        with self.assertRaisesRegex(Http404, "Категории с таким id не существует в меню."):
            get_all_dishes_from_category_or_404(category_id=9999959996999999)

    def test_get_dish_description_or_404(self) -> None:
        self.assertEqual(type(get_dish_description_or_404(dish_id=self.test_dish.id)), QuerySet)
        with self.assertRaisesRegex(Http404, "Блюдо с таким id не существует в меню."):
            get_dish_description_or_404(dish_id=9999959996999999)

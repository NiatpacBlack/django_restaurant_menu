from django.urls import reverse
from rest_framework.test import APITestCase

from menu.models import MenuCategoriesModel, DishesModel


class MenuServicesTest(APITestCase):
    """Тесты API. Для работы тестов в меню будут временно добавлены категория и блюдо."""

    def setUp(self) -> None:
        MenuCategoriesModel.objects.create(category_name="APITestCategory999")
        self.test_category = MenuCategoriesModel.objects.filter(category_name="APITestCategory999").first()
        DishesModel.objects.create(
            dish_name="APITestDish999",
            category_id=self.test_category.id,
            price=4.5,
            description="Тестовое описание" * 100,
        )
        self.test_dish = DishesModel.objects.filter(dish_name="APITestDish999").first()

    def test_menu_get(self):
        url = reverse('api_menu')
        response = self.client.get(url)
        print(response)

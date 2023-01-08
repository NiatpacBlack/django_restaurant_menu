from django.http import HttpRequest, HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView

from api.serializers import MenuCategoriesSerializer, FullDishesSerializer, SimpleDishesSerializer
from menu.services import get_all_categories_from_menu, get_all_dishes_from_menu, get_all_dishes_from_category_or_404, \
    get_not_empty_category_id, get_dish_description_or_404
from reports.services import add_selection_in_selection_dishes_table


class MenuCategoriesViewSet(viewsets.ModelViewSet):
    """APi представление позволяющее работать с данными модели MenuCategories."""
    queryset = get_all_categories_from_menu()
    serializer_class = MenuCategoriesSerializer


class DishesViewSet(viewsets.ModelViewSet):
    """APi представление позволяющее работать с данными модели MenuCategories."""
    queryset = get_all_dishes_from_menu()
    serializer_class = FullDishesSerializer


class MenuView(APIView):
    """APi представление возвращающее данные о не пустых категориях из меню."""

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        queryset = [el for el in get_all_categories_from_menu() if el.id in get_not_empty_category_id()]
        serializer = MenuCategoriesSerializer(queryset, many=True)
        return HttpResponse(serializer.data)


class DishesView(APIView):
    """Api представление возвращающее данные о блюдах из определенной категории."""

    @staticmethod
    def get(request: HttpRequest, category_id: int) -> HttpResponse:
        queryset = get_all_dishes_from_category_or_404(category_id=category_id)
        serializer = SimpleDishesSerializer(queryset, many=True)
        return HttpResponse(serializer.data)


class DishDescriptionView(APIView):
    """
    Api представление возвращающее данные с описанием конкретного блюда с dish_id.

    При получении информации о блюде, в таблицу со статистикой нажатий добавляется запись о пользователе и блюде.
    """

    @staticmethod
    def get(request: HttpRequest, category_id: int, dish_id: int) -> HttpResponse:
        queryset = get_dish_description_or_404(dish_id=dish_id)
        add_selection_in_selection_dishes_table(request.user, dish_id)
        serializer = FullDishesSerializer(queryset, many=True)
        return HttpResponse(serializer.data)

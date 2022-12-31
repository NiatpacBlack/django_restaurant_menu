from django.shortcuts import render
from django.views import View

from menu.services import (
    get_all_categories_from_menu,
    get_all_dishes_from_category_or_404,
    get_dish_description_or_404, get_not_empty_category_id,
)
from reports.services import (
    add_selection_in_selection_dishes_table,
    get_dish_report_data,
)


class MenuPageView(View):
    """Функции обрабатывающие запросы приходящие при открытии главной страницы сайта."""

    @staticmethod
    def get(request):
        """При открытии страницы сайта отображает шаблон с кнопками соответствующими не пустым категориям меню."""
        return render(
            request,
            "menu/categories_page.html",
            context={
                "categories": get_all_categories_from_menu(),
                "list_not_empty_category_id": get_not_empty_category_id(),
            },
        )


class DishesPageView(View):
    """Функции, обрабатывающие запросы приходящие при открытии определенной категории."""

    @staticmethod
    def get(request, category_id):
        """При открытии категории отображает шаблон с кнопками соответствующими блюдам в этой категории."""
        queryset = get_all_dishes_from_category_or_404(category_id)
        return render(
            request,
            "menu/dishes_page.html",
            context={
                "dishes": queryset,
            },
        )


class DishDescriptionPageView(View):
    """Функции, обрабатывающие запросы приходящие при открытии определенного блюда."""

    @staticmethod
    def get(request, dish_id):
        """При открытии блюда, отображает описание этого блюда."""
        queryset = get_dish_description_or_404(dish_id)
        add_selection_in_selection_dishes_table(request.user, dish_id)
        return render(
            request,
            "menu/dish_description_page.html",
            context={
                "dish": queryset,
            },
        )

    def post(self, request, dish_id):
        """Получает название отчета из post запроса, и выводит пользователю соответсвующий график."""
        report_data = get_dish_report_data(
            report_name=self.request.POST["action"], dish_id=dish_id
        )
        if report_data:
            queryset = get_dish_description_or_404(dish_id)
            return render(
                request,
                "menu/dish_description_page.html",
                context={
                    "dish": queryset,
                    "action": True,
                    "report_name": report_data["report_title"],
                    "x_axis": report_data["x_axis"],
                    "data": report_data["report_data"],
                },
            )

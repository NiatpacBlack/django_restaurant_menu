from django.shortcuts import render
from django.views import View

from reports.services import get_top_dishes_data, get_top_users_data, get_top_users_from_category
from .forms import DishesForm


class TopDishReportView(View):
    """Функции обрабатывающие запросы приходящие при открытии отчета по самым популярным блюдам."""

    @staticmethod
    def get(request):
        """При открытии страницы с отчетом отображает шаблон с формой настройки параметров отчета."""
        return render(request, 'reports/data_and_limit_for_report_form.html')

    def post(self, request):
        """
        Выводит шаблон с отчетом по популярным товарам в виде графика.

        Передает в шаблон данные заполненной формы с информацией о диапазоне дат отчета и количестве элементов выборки.
        """
        calendar_from = self.request.POST['calendar_from']
        calendar_to = self.request.POST['calendar_to']
        max_elements = self.request.POST['max_elements']

        top_dishes_data = get_top_dishes_data(calendar_from, calendar_to, max_elements)

        return render(request, 'reports/diagram_report_of_popular_positions.html', context={
            "top_position_data": top_dishes_data,
            "report_title": f'Топ {max_elements} блюд за период с {calendar_from} по {calendar_to}',
            "report_info": 'График отображает популярные блюда на основе количества нажатий на каждое блюдо в меню.',
            "column_name": "Товар",
        })


class TopUserReportView(View):
    """Методы, обрабатывающие запросы при открытии отчета по самым популярным пользователям."""

    @staticmethod
    def get(request):
        """При открытии страницы с отчетом отображает шаблон с формой настройки параметров отчета."""
        return render(request, 'reports/data_and_limit_for_report_form.html')

    def post(self, request):
        """
        Выводит шаблон с отчетом по популярным пользователям сайта в виде графика.

        Передает в шаблон данные заполненной формы с информацией о диапазоне дат отчета и количестве элементов выборки.
        """
        calendar_from = self.request.POST['calendar_from']
        calendar_to = self.request.POST['calendar_to']
        max_elements = self.request.POST['max_elements']

        top_users_data = get_top_users_data(calendar_from, calendar_to, max_elements)

        return render(request, 'reports/diagram_report_of_popular_positions.html', context={
            "top_position_data": top_users_data,
            "report_title": f'Топ {max_elements} пользователей за период с {calendar_from} по {calendar_to}',
            "report_info": 'График отображает популярных пользователей на основе количества нажатий на блюдо в меню.',
            "column_name": "Пользователь",
        })


class TopUserFromCategoryReportView(View):
    """Методы, обрабатывающие запросы, при открытии отчета по самым популярным пользователям в выбранной категории."""

    @staticmethod
    def get(request):
        """При открытии страницы с отчетом отображает шаблон с формой настройки параметров отчета."""
        form = DishesForm()
        return render(request, 'reports/top_users_from_category_form.html', context={
            "category_form": form,
        })

    def post(self, request):
        """
        Выводит шаблон, с отчетом по популярным пользователям в определенной категории меню, в виде графика.

        Передает в шаблон данные заполненной формы с информацией о диапазоне дат отчета, id категории
        и количестве элементов выборки.
        """
        category_id = self.request.POST['category']
        calendar_from = self.request.POST['calendar_from']
        calendar_to = self.request.POST['calendar_to']
        max_elements = self.request.POST['max_elements']
        top_users_data = get_top_users_from_category(calendar_from, calendar_to, category_id, max_elements)

        return render(request, 'reports/diagram_report_of_popular_positions.html', context={
            "top_position_data": top_users_data,
            "report_title": f'Топ {max_elements} пользователей в категории {top_users_data[0]["category"]} за период с {calendar_from} по {calendar_to}',
            "report_info": 'График отображает популярных пользователей, в определенной категории блюд, на основе количества нажатий на блюдо в меню.',
            "column_name": "Пользователь",
        })

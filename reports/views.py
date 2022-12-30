from pprint import pprint

from django.shortcuts import render
from django.views import View

from reports.services import get_top_dishes_data


class TopDishReportView(View):
    """Функции обрабатывающие запросы приходящие при открытии отчета по самым популярным блюдам."""

    @staticmethod
    def get(request):
        """При открытии страницы с отчетом отображает шаблон с формой настройки параметров отчета."""
        return render(request, 'reports/top_dishes_report_form.html')

    def post(self, request):
        """
        Выводит шаблон с отчетом в виде графика.

        Передает в шаблон данные заполненной формы с информацией о диапазоне дат отчета и количестве элементов выборки.
        """
        calendar_from = self.request.POST['calendar_from']
        calendar_to = self.request.POST['calendar_to']
        max_elements = self.request.POST['max_elements']

        top_dishes_data = get_top_dishes_data(calendar_from, calendar_to, max_elements)

        return render(request, 'reports/top_dishes_report.html', context={
            "top_dishes_data": top_dishes_data,
            "calendar_from": calendar_from,
            "calendar_to": calendar_to,
        })

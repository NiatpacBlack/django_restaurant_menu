from django.shortcuts import render
from django.views import View


class TopDishReportView(View):
    """Функции обрабатывающие запросы приходящие при открытии отчета по самым популярным блюдам."""

    @staticmethod
    def get(request):
        """При открытии страницы с отчетом отображает шаблон с данными о самых популярных блюдах."""
        pass

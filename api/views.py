from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import MenuPageSerializer
from menu.services import get_all_categories_from_menu


class MenuPageApiView(APIView):
    """APi представление возвращающее данные о категориях из меню."""

    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        queryset = get_all_categories_from_menu()
        serializer = MenuPageSerializer(queryset, many=True)
        return Response(serializer.data)

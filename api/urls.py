from django.urls import path
from . import views


urlpatterns = [
    path("", views.MenuPageApiView.as_view(), name="api_menu"),
]

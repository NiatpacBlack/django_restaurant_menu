from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers

from . import views


routers = routers.SimpleRouter()
routers.register(r'menu_categories', views.MenuCategoriesViewSet)
routers.register(r'menu_dishes', views.DishesViewSet)

urlpatterns = [
    path("", include(routers.urls), name="api_menu_table"),
    path("", login_required(views.MenuView.as_view()), name="api_menu"),
    path("category/<int:category_id>/", login_required(views.DishesView.as_view()), name="api_dishes"),
    path("dish/<int:dish_id>/", login_required(views.DishDescriptionView.as_view()),
         name="api_dish_description"),
]

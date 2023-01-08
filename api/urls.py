from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib.auth.decorators import login_required


routers = routers.DefaultRouter()
routers.register(r'menu_categories', views.MenuCategoriesViewSet)
routers.register(r'menu_dishes', views.DishesViewSet)

urlpatterns = [
    path("", include(routers.urls), name="api_menu_table"),
    path("menu/", login_required(views.MenuView.as_view()), name="api_menu"),
    path("menu/<int:category_id>/", login_required(views.DishesView.as_view()), name="api_dishes"),
    path("menu/<int:category_id>/<int:dish_id>/", login_required(views.DishDescriptionView.as_view()),
         name="api_dish_description"),
]

from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    path("", login_required(views.MenuPageView.as_view()), name="menu"),
    path(
        "category_<int:category_id>",
        login_required(views.DishesPageView.as_view()),
        name="category",
    ),
    path(
        "dish_<int:dish_id>",
        login_required(views.DishDescriptionPageView.as_view()),
        name="dish",
    ),
]

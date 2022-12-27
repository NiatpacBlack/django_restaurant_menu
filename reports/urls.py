from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views


urlpatterns = [
    path("top_dishes_report", login_required(views.TopDishReportView.as_view()), name='top_dishes_report'),
]

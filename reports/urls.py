from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path

from . import views


urlpatterns = [
    path("top_dishes_report", staff_member_required(views.TopDishReportView.as_view()), name='top_dishes_report'),
    path("top_users_report", staff_member_required(views.TopUserReportView.as_view()), name='top_users_report'),
]

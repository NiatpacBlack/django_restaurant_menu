from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/reports/", include("reports.urls")),
    path("", include("menu.urls")),
    path("api/menu/", include("menu.api.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]

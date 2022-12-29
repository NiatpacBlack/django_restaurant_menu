from django.contrib import admin

from .models import SelectionDishesModel


@admin.register(SelectionDishesModel)
class SelectionDishesAdmin(admin.ModelAdmin):
    search_fields = ("username__username",)
    list_display = ("dish", "selection_time", "username")
    list_filter = ("username",)

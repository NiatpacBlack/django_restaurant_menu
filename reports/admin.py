from django.contrib import admin

from .models import SelectionDishesModel


@admin.register(SelectionDishesModel)
class SelectionDishesAdmin(admin.ModelAdmin):
    pass

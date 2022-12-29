from django.contrib import admin

from .models import MenuCategoriesModel, DishesModel


@admin.register(MenuCategoriesModel)
class MenuCategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(DishesModel)
class DishesAdmin(admin.ModelAdmin):
    pass

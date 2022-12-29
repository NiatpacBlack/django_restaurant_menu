from django.contrib import admin

from .models import MenuCategoriesModel, DishesModel


@admin.register(MenuCategoriesModel)
class MenuCategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(DishesModel)
class DishesAdmin(admin.ModelAdmin):
    list_display = ("dish_name", "price", "category")
    list_filter = ("category",)

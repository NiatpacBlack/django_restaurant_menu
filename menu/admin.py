from django.contrib import admin

from .models import MenuCategoriesModel, DishesModel


class MenuCategoriesAdmin(admin.ModelAdmin):
    pass


class DishesAdmin(admin.ModelAdmin):
    pass


admin.site.register(MenuCategoriesModel, MenuCategoriesAdmin)
admin.site.register(DishesModel, DishesAdmin)

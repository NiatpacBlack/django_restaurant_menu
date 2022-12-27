from django.contrib import admin

from .models import SelectionDishesModel


class SelectionDishesAdmin(admin.ModelAdmin):
    pass


admin.site.register(SelectionDishesModel, SelectionDishesAdmin)

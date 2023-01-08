from rest_framework import serializers
from menu.models import MenuCategoriesModel, DishesModel


class MenuCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategoriesModel
        fields = '__all__'


class FullDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishesModel
        fields = '__all__'


class SimpleDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishesModel
        fields = ['id', 'dish_name']

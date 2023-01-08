from rest_framework import serializers
from menu.models import MenuCategoriesModel


class MenuPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategoriesModel
        fields = ['id', 'category_name']

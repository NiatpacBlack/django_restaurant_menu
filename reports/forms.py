from django.forms import ModelForm

from menu.models import DishesModel


class DishesForm(ModelForm):
    """Форма, отображающая choicefield поле с выбором существующей категории из меню."""
    class Meta:
        model = DishesModel
        fields = ['category']

from django.forms import ModelForm
from foodmarket.models import Dish, Review

class NowOrderDishForm(ModelForm):
    class Meta:
        model = Dish
        fields = [
            'name',
            'price',
            'num_for_sale',
            'image_url',
            'allergy_info']

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'rating',
            'comment']
from django import forms

class AddDishForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=4, decimal_places=2, min_value=0)
    image = forms.ImageField()
    allergy_info = forms.CharField(max_length=200)

class AddNowOrderDishForm(AddDishForm):
    num_for_sale = forms.IntegerField(min_value=0)

class AddReviewForm(forms.Form):
    rating = forms.IntegerField()
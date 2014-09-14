from django import forms

class AddDishForm(forms.Form):
    price = forms.DecimalField(max_digits=4, decimal_places=2)
    allergy_info = forms.CharField(max_length=200)

class AddNowOrderDishForm(AddDishForm):
    num_for_sale = forms.IntegerField()

class AddReviewForm(forms.Form):
    rating = forms.IntegerField()
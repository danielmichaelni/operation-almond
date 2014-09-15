from django.shortcuts import render
from foodmarket.models import UserProfile, Vendor, Dish, PreOrderDish, NowOrderDish, Review
from foodmarket import forms

def index(request):
    return render(request, 'foodmarket/index.html')

def browse(request):
    dishes = Dish.objects.filter(available=True)
    return render(request, 'foodmarket/browse.html', {'dishes': dishes})

def dish_detail(request): # todo
    return render(request, 'foodmarket/index.html')

def kitchen(request):
    return render(request, 'foodmarket/kitchen.html')

def add_inventory(request):
    form = forms.AddNowOrderDishForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        price = form.cleaned_data['price']
        allergy_info = form.cleaned_data['allergy_info']
        num_for_sale = form.cleaned_data['num_for_sale']

        return render(request, 'foodmarket/test.html', {'test': 'added inventory'})

    return render(request, 'foodmarket/add_inventory.html', {'form': form})
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
    form = forms.AddNowOrderDishForm()
    return render(request, 'foodmarket/add_inventory.html', {'form': form})
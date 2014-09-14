from django.shortcuts import render
from foodmarket.models import UserProfile, Vendor, Dish, PreOrderDish, NowOrderDish, Review

def index(request):
    return render(request, 'foodmarket/index.html')

def browse(request):
    dishes = Dish.objects.filter(available=True)
    return render(request, 'foodmarket/browse.html', {'dishes': dishes})

def kitchen(request):
    return render(request, 'foodmarket/kitchen.html')

def add_inventory(request):
    return render(request, 'foodmarket/add_inventory.html')

def start_kitchen(request):
    pass
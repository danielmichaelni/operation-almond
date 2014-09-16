from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from foodmarket.models import UserProfile, Vendor, Dish, PreOrderDish, NowOrderDish, Review
from foodmarket import forms

def index(request):
    return render(request, 'foodmarket/index.html')

#def login_required(request):
#    pass

def browse(request):
    dishes = Dish.objects.filter(available=True)
    return render(request, 'foodmarket/browse.html', {'dishes': dishes})

def dish_detail(request, dish_id): # todo
    dish = get_object_or_404(NowOrderDish, pk=dish_id)
    return render(request, 'foodmarket/index.html')

def dish_reviews(request): # todo
    return render(request, 'foodmarket/index.html')

def review_detail(request): # todo
    return render(request, 'foodmarket/index.html')

@login_required
def kitchen(request):
    return render(request, 'foodmarket/kitchen.html')

@login_required
def add_inventory(request):
    form = forms.NowOrderDishForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        num_for_sale = form.cleaned_data['num_for_sale']
        image_url = form.cleaned_data['image_url']
        allergy_info = form.cleaned_data['allergy_info']

        d = NowOrderDish(name=name, price=price, num_for_sale=num_for_sale, image_url=image_url, allergy_info=allergy_info)

        return render(request, 'foodmarket/test.html', {'test': name})
    return render(request, 'foodmarket/add_inventory.html', {'form': form})
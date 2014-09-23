from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from foodmarket.models import UserProfile, Vendor, Dish, Review
from foodmarket.decorators import venmo_authorized
from foodmarket import forms
import requests

def index(request):
    return render(request, 'foodmarket/index.html')

def browse(request):
    dishes = Dish.objects.filter(available=True)
    return render(request, 'foodmarket/browse.html', {'dishes': dishes})

def dish_detail(request, dish_id): # todo
    dish = get_object_or_404(Dish, pk=dish_id)
    return render(request, 'foodmarket/dish_detail.html', {'dish': dish})

@login_required
@venmo_authorized
def order_dish(request, dish_id):
    dish = get_object_or_404(Dish, pk=dish_id)
    data = {
        'access_token': request.user.profile.venmo_access_token,
        'user_id': settings.VENMO_PAY_TO_USER_ID,
        'note': 'buying ' + dish.name + ' from ' + dish.vendor.user.username,
        'amount': dish.price,
        'audience': 'private'}
    url = 'https://api.venmo.com/v1/payments'
    response = requests.post(url, data)
    response_dict = response.json()
    return redirect('/')

def dish_reviews(request): # todo
    return render(request, 'foodmarket/index.html')

def review_detail(request): # todo
    return render(request, 'foodmarket/index.html')

@login_required
def profile(request):
    payload = {
        'client_id': settings.VENMO_ID,
        'scope': 'make_payments',
        'response_type': 'code'}
    r = requests.get('https://api.venmo.com/v1/oauth/authorize', params=payload)
    return render(request, 'foodmarket/profile.html', {'venmo_authorization_url': r.url})

@login_required
def venmo_authorization(request):
    venmo_authorization_code = request.GET.get('code')
    data = {
        'client_id': settings.VENMO_ID,
        'client_secret': settings.VENMO_SECRET,
        'code': venmo_authorization_code}
    url = 'https://api.venmo.com/v1/oauth/access_token'
    response = requests.post(url, data)
    response_dict = response.json()
    p = request.user.profile
    p.venmo_id = response_dict['user']['id']
    p.venmo_access_token = response_dict['access_token']
    p.venmo_refresh_token = response_dict['refresh_token']
    p.save()
    return redirect('/profile')

@login_required
@venmo_authorized
def kitchen(request):
    dishes = request.user.vendor.dish.all()
    return render(request, 'foodmarket/kitchen.html', {'dishes': dishes})

@login_required
def add_inventory(request):
    form = forms.NowOrderDishForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        vendor = request.user.vendor
        name = form.cleaned_data['name']
        price = form.cleaned_data['price']
        num_for_sale = form.cleaned_data['num_for_sale']
        image_url = form.cleaned_data['image_url']
        allergy_info = form.cleaned_data['allergy_info']
        available = num_for_sale > 0

        d = Dish(
            vendor=vendor,
            name=name,
            price=price,
            num_for_sale=num_for_sale,
            image_url=image_url,
            allergy_info=allergy_info,
            available=available)
        d.save()

        return redirect('/dish/%d' % d.id)
    return render(request, 'foodmarket/add_inventory.html', {'form': form})
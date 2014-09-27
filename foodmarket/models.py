from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields.encrypted import EncryptedCharField
from decimal import Decimal
from payments import PurchasedItem
from payments.models import BasePayment
import requests

class Payment(BasePayment):
    
    def get_failure_url(self):
        return 'http://operationalmond.herokuapp.com/failure/'

    def get_success_url(self):
        return 'http://operationalmond.herokuapp.com/success/'

    def get_purchased_items(self):
        # you'll probably want to retrieve these from an associated order
        yield PurchasedItem(name='The Hound of the Baservilles', sku='BSKV',
                            quantity=9, price=Decimal(10), currency='USD')

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='vendor')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)

User.vendor = property(lambda u: Vendor.objects.get_or_create(user=u)[0])

class Dish(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='dish')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Price ($)')
    image_url = models.URLField(blank=True, verbose_name='Image URL (optional)')
    allergy_info = models.CharField(max_length=200)
    available = models.BooleanField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    require_pre_order = models.BooleanField(default=False)

    # now-order dish
    num_for_sale = models.IntegerField(null=True, verbose_name='Number for sale')

    # pre-order dish
    deadline_to_order = models.DateTimeField(null=True)
    availability_date = models.DateTimeField(null=True)
    num_available = models.IntegerField(null=True)

class Review(models.Model):
    dish = models.ForeignKey(Dish)
    user = models.ForeignKey(User)
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000)
    published_date = models.DateTimeField(auto_now_add=True)
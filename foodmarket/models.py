from django.db import models
from django.contrib.auth.models import User
import requests

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    venmo_id = models.CharField(max_length=200)
    venmo_access_token = models.CharField(max_length=200)
    venmo_refresh_token = models.CharField(max_length=200)

    def venmo_authorized(self):
        if self.venmo_access_token:
            return True
        return False

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

    #require_pre_order = models.BooleanField(default=False)

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
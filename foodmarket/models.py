from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Vendor(models.Model):
    user = models.OneToOneField(UserProfile)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

class Dish(models.Model):
    vendor = models.ForeignKey(Vendor)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    allergy_info = models.CharField(max_length=200)
    available = models.BooleanField()

class PreOrderDish(Dish): # for later
    deadline_to_order = models.DateTimeField()
    availability_date = models.DateTimeField()
    num_available = models.IntegerField()

class NowOrderDish(Dish):
    num_for_sale = models.IntegerField()

class Review(models.Model):
    dish = models.ForeignKey(Dish)
    user = models.ForeignKey(User)
    rating = models.IntegerField()
    published_date = models.DateTimeField(auto_now_add=True)
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

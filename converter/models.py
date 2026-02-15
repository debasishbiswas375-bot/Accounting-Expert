from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=100)
    is_pro = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Topic(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    is_pro = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # FIX: Required for admin panel

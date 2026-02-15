from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=100)
    is_pro = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.credits} Credits"

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Custom business fields synced with Streamlit
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    # Required to prevent clash with default Django User
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True
    )

class UserProfile(models.Model):
    # Links a credit plan to each user
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    credits = models.IntegerField(default=100)
    plan_name = models.CharField(max_length=50, default='Starter')
    is_pro = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.plan_name}"

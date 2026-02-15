from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # If you added extra fields, add them here
    fieldsets = UserAdmin.fieldsets + (
        # ('Extra Info', {'fields': ('phone_number',)}),
    )

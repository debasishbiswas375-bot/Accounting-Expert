from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Plan


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": (
                "phone",
                "country",
                "state",
                "city",
                "plan",
            )
        }),
    )

    list_display = (
        "username",
        "email",
        "phone",
        "country",
        "city",
        "plan",
        "is_staff",
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Plan)

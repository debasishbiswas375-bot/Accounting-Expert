from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User

# Automatically creates your admin user on startup
def auto_create_admin():
    try:
        if not User.objects.filter(username="admin").exists():
            # Using your password: Deba9002043666
            User.objects.create_superuser("admin", "admin@example.com", "Deba9002043666")
    except Exception:
        pass

auto_create_admin()

# Portal Branding
admin.site.site_header = "Accounting Expert Admin Portal"
admin.site.site_title = "Accounting Expert Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from converter import views

# Renaming the Admin Portal Titles
admin.site.site_header = "Accounting Expert Admin Portal"
admin.site.site_title = "Accounting Expert Admin Portal"
admin.site.index_title = "Welcome to the Accounting Expert Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
]
from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "Deba@123")
        return HttpResponse("Superuser 'admin' created successfully!")
    return HttpResponse("Superuser already exists.")

# Add this to your urlpatterns list:
# path('create-admin-secure-99/', create_admin),

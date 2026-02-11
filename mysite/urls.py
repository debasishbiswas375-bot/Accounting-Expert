# mysite/urls.py
from django.contrib import admin
from django.urls import path
from converter import views

# Renaming the Admin Site
admin.site.site_header = "Accounting Expert Admin Portal"
admin.site.site_title = "Accounting Expert Admin Portal"
admin.site.index_title = "Welcome to the Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
]

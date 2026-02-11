# mysite/urls.py
from django.contrib import admin
from django.urls import path, include

# Renaming the Admin Site - Eye-catching titles
admin.site.site_header = "Accounting Expert Admin Portal"
admin.site.site_title = "Accounting Expert Admin"
admin.site.index_title = "Welcome to your Financial Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    # include your other app urls here
]

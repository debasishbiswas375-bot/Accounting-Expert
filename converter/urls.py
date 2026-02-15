from django.urls import path, include

urlpatterns = [
    path('', include('converter.urls')),  # ❌ this line is failing
]

from django.shortcuts import render

def home(request):
    # Renders converter/templates/home.html
    return render(request, 'home.html')

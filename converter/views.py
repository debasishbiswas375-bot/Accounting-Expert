from django.shortcuts import render
from django.http import HttpResponse

# Home page view
def home(request):
    return render(request, 'home.html')  # Looks for converter/templates/home.html

# Convert page view
def convert(request):
    # Example: you can add your conversion logic later
    if request.method == 'POST':
        # handle form submission here
        return HttpResponse("Conversion logic goes here")
    return render(request, 'convert.html')  # create converter/templates/convert.html

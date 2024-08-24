from django.shortcuts import render
from django.http import HttpResponse  # Corrected import statement

def home(request):
    return HttpResponse("Hello, World!") 
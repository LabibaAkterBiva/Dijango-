from django.shortcuts import render

def about(request):
    return render(request, "first_app/about.html")
def contact(request):
    return render(request, "first_app/contact.html")

# Create your views here.

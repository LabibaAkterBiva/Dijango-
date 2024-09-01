from django.shortcuts import render
from musician.models import Musician


def home(request):
    data = Musician.objects.prefetch_related('album_set').all()
    return render(request, 'home.html',{'data':data})
    
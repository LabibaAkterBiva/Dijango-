from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.rhome, name='home'),
    path('meal/', views.index, name='meal'),
    
]

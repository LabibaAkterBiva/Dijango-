
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='res'),
    path('home/',include('meal.urls')),
    path('about_us/',include('about_us.urls')),
]


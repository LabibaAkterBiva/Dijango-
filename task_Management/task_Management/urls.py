
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='homepage'),
    path('task/', include('task.urls')),
    path('task_category/', include('task_category.urls')),
   
]

from django.urls import path,include
from.import views
urlpatterns = [
path('add/',views.add_music,name='add_music'),
path('edit/<int:id>',views.edit_music,name='edit_music'),
path('delete/<int:id>',views.delete_music,name='delete_music'),
 
]



 

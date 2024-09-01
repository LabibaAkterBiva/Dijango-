from django.urls import path,include
from.import views
urlpatterns = [

path('register/',views.UserRegistrationView.as_view(),name='register'),
path('login/',views.UserLogin.as_view(),name='user_login'),
path('logout/',views.user_logout,name='user_logout'),
path('profile/',views.ProfileView.as_view(),name='profile'),
]

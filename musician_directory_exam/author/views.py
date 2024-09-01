from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
class CreateUserView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('add_musician')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context

class UserRegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    def form_valid(self, form):
        messages.success(self.request,"Account created successfully")
        return super().form_valid(form) 
    def form_invalid(self, form):
        messages.success(self.request,"Give valid information")
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context 
    
class UserLogin(LoginView):
     template_name='register.html'


     def form_valid(self, form):
         messages.success(self.request,"Logged in successfully")
         return super().form_valid(form)
     def form_invalid(self, form):
          messages.success(self.request,"Logged in information incorrect")
          return super().form_invalid(form)
     def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["type"] =' login'
         return context
     def  get_success_url(self):
          return reverse_lazy('profile')     
@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'
    reverse_lazy='home'


def user_logout(request):
     logout(request)
     messages.success(request,"Logged out successfully")
     return redirect('user_login')

                    

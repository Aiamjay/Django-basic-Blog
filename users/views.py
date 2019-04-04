from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = 'post_list'
    # redirect_field_name = 'post_list'


class UserLogoutView(LogoutView):
    next_page = '/'


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

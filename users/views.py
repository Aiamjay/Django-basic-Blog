from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import CustomUserCreationForm


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('blog:post_list')


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

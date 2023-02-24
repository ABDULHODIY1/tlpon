from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from .forms import CustomUserCreateForm
from django.urls import reverse_lazy
# Create your views here.

class SingUpView(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'



class UserHome(TemplateView):
    template_name = 'users/users.html'
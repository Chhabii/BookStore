from django.shortcuts import render
from django.views import generic 
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from django.core.mail import send_mail
from django.conf import settings

class SignUpPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name='signup.html'



from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm,CustomAuthenticationForm, CustomUserCreationBenForm

class SignUpBen(CreateView):
    form_class = CustomUserCreationBenForm
    success_url = reverse_lazy("sigin")
    template_name = 'signup.html'

class SignUpDon(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("sigin")
    template_name = 'signup.html'

class SigIn(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'
from django import forms
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm,CustomAuthenticationForm, CustomUserCreationBenForm, CustomInstitutionForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Beneficiary, Institution, LegalDonor, NaturalDonor



class SignUpBen(CreateView):
    form_class = CustomUserCreationBenForm
    success_url = reverse_lazy("users:sigin")
    template_name = 'signup.html'

class SignUpDon(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:sigin")
    template_name = 'signup.html'

class SignUpIns(CreateView):
    form_class = CustomInstitutionForm
    success_url = reverse_lazy("users:sigin")
    template_name = 'signup.html'

class SigIn(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'


class BeneficiaryUpdateForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['email', 'name', 'idType', 'numID', 'birth_date', 'gender','profilePicture']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'idType': forms.Select(attrs={'class': 'form-select'}),
            'numID': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'profilePicture':forms.FileInput(attrs={'class': 'form-control'}),
        }


class BeneficiaryUpdateView(UpdateView):
    model = Beneficiary
    form_class = BeneficiaryUpdateForm
    template_name = 'user_update.html'

    def get_success_url(self):
        return reverse_lazy("scholarships:showmenu")
    

class NaturalDonorUpdateForm(forms.ModelForm):
    class Meta:
        model = NaturalDonor
        fields = ['email', 'name', 'idType', 'numID', 'profilePicture']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'idType': forms.Select(attrs={'class': 'form-select'}),
            'numID': forms.TextInput(attrs={'class': 'form-control'}),
            'profilePicture':forms.FileInput(attrs={'class': 'form-control'}),
        }

class NaturalDonorUpdateView(UpdateView):
    model = NaturalDonor
    form_class = NaturalDonorUpdateForm
    template_name = 'user_update.html'

    def get_success_url(self):
        return reverse_lazy("scholarships:showmenu")
    
class LegalDonorUpdateForm(forms.ModelForm):
    class Meta:
        model = LegalDonor
        fields = ['email', 'name', 'idType', 'numID','description', 'profilePicture']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'idType': forms.Select(attrs={'class': 'form-select'}),
            'numID': forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'profilePicture':forms.FileInput(attrs={'class': 'form-control'}),
        }

class LegalDonorUpdateView(UpdateView):
    model = LegalDonor
    form_class = NaturalDonorUpdateForm
    template_name = 'user_update.html'

    def get_success_url(self):
        return reverse_lazy("scholarships:showmenu")
    
class InstitutionUpdateForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['email', 'name', 'idType', 'numID','description', 'profilePicture']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'idType': forms.Select(attrs={'class': 'form-select'}),
            'numID': forms.TextInput(attrs={'class': 'form-control'}),
            'type_institution':forms.Select(attrs={'class': 'form-select'}),
            'city': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'profilePicture':forms.FileInput(attrs={'class': 'form-control'}),
        }

class InstitutionUpdateView(UpdateView):
    model = Institution
    form_class = InstitutionUpdateForm
    template_name = 'user_update.html'

    def get_success_url(self):
        return reverse_lazy("scholarships:showmenu")
    

from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm,CustomAuthenticationForm, CustomUserCreationBenForm
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

class SigIn(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'login.html'

class BeneficiaryUpdateView(UpdateView):
    model = Beneficiary
    template_name = 'user_update.html'
    fields = ['email', 'name', 'idType', 'numID','birth_date', 'gender','profilePicture']  # Agrega los campos necesarios

    def get_success_url(self):
        return reverse_lazy('users:beneficiary_detail', kwargs={'pk': self.object.pk})

class NaturalDonorUpdateView(UpdateView):
    model = NaturalDonor
    template_name = 'user_update.html'
    fields = ['email','name','idType', 'numID', 'profilePicture']  # Agrega los campos necesarios

    def get_success_url(self):
        return reverse_lazy('users:natural_donor_detail', kwargs={'pk': self.object.pk})

class LegalDonorUpdateView(UpdateView):
    model = LegalDonor
    template_name = 'user_update.html'
    fields = ['email','name','idType', 'numID', 'description', 'profilePicture']  # Agrega los campos necesarios

    def get_success_url(self):
        return reverse_lazy('users:legal_donor_detail', kwargs={'pk': self.object.pk})

class InstitutionUpdateView(UpdateView):
    model = Institution
    template_name = 'user_update.html'
    fields = ['email','name','idType', 'numID','type_institution', 'city', 'description','address', 'profilePicture']  # Agrega los campos necesarios

    def get_success_url(self):
        return reverse_lazy('users:institution_detail', kwargs={'pk': self.object.pk})
    
"""""
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Beneficiary, NaturalDonor, LegalDonor, Institution

class BeneficiaryListView(ListView):
    model = Beneficiary
    template_name = 'users/beneficiary_list.html'
    context_object_name = 'beneficiaries'

class BeneficiaryDetailView(DetailView):
    model = Beneficiary
    template_name = 'users/beneficiary_detail.html'
    context_object_name = 'beneficiary'

class BeneficiaryCreateView(CreateView):
    model = Beneficiary
    template_name = 'users/beneficiary_create.html'
    fields = ['email', 'name', 'idType', 'numID', 'role', 'birth_date', 'gender']
    success_url = reverse_lazy('users:beneficiary_list')

class BeneficiaryUpdateView(UpdateView):
    model = Beneficiary
    template_name = 'users/beneficiary_update.html'
    fields = ['email', 'name', 'idType', 'numID', 'role', 'birth_date', 'gender']
    success_url = reverse_lazy('users:beneficiary_list')

class BeneficiaryDeleteView(DeleteView):
    model = Beneficiary
    template_name = 'users/beneficiary_delete.html'
    success_url = reverse_lazy('users:beneficiary_list')

# Repite las mismas vistas para los otros tipos de usuarios (NaturalDonor, LegalDonor, Institution)"""

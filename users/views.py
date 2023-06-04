from django import forms
from django.shortcuts import redirect

from django.views import View
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm,CustomAuthenticationForm, CustomUserCreationBenForm, CustomInstitutionForm
from .forms import LegalDonorForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Beneficiary, Institution, LegalDonor, NaturalDonor, User



class SignUpBen(CreateView):
    form_class = CustomUserCreationBenForm
    success_url = reverse_lazy("users:sigin")
    template_name = 'signup.html'

    def form_valid(self, form):
        # Crea una instancia del modelo User con los datos del formulario
        user = form.save(commit=False)

        # Establece el campo 'role' como User.BENEFICIARY
        user.role = User.BENEFICIARY

        # Guarda el usuario en la base de datos
        user.save()

       
        return super().form_valid(form)

class SignUpDon(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users:sigin")
    template_name = 'signup.html'

    def form_valid(self, form):
        # Crea una instancia del modelo User con los datos del formulario
        user = form.save(commit=False)

        # Establece el campo 'role' como User.NATURALDONOR
        user.role = User.NATURALDONOR

        # Guarda el usuario en la base de datos
        user.save()

       
        return super().form_valid(form)

class SignUpLegalDon(CreateView):
    form_class = LegalDonorForm
    success_url = reverse_lazy("users:sigin")
    template_name = 'signup.html'

    def form_valid(self, form):
        # Crea una instancia del modelo User con los datos del formulario
        user = form.save(commit=False)

        # Establece el campo 'role' como User.LEGALDONOR
        user.role = User.LEGALDONOR

        # Guarda el usuario en la base de datos
        user.save()

       
        return super().form_valid(form)        

class SignUpIns(CreateView):
    form_class = CustomInstitutionForm
    success_url = reverse_lazy("users:sigin")
    template_name = 'signup.html'

    def form_valid(self, form):
        # Crea una instancia del modelo User con los datos del formulario
        user = form.save(commit=False)

        # Establece el campo 'role' como User.INSTITUTION
        user.role = User.INSTITUTION

        # Guarda el usuario en la base de datos
        user.save()

        
        return super().form_valid(form)
    

    

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

class UserListView(ListView):
    model = User
    template_name = 'usersList.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(role=User.INSTITUTION)
    
class InstitutionVerifyView(View):
    def get(self, request, pk):
        institution = Institution.objects.get(pk=pk)
        institution.verificationState = 'A'  # Cambiar estado de verificación a 'Aprobada'
        institution.save()
        return redirect('scholarships:look_institutions')  # Redirigir a la lista de instituciones

class InstitutionRejectVerificationView(View):
    def get(self, request, pk):
        institution = Institution.objects.get(pk=pk)
        institution.verificationState = 'R'  # Cambiar estado de verificación a 'Rechazada'
        institution.save()
        return redirect('scholarships:look_institutions')  # Redirigir a la lista de instituciones


class AllUserListView(View):
    template_name = 'showUsers.html'

    def get(self, request):
        users = User.objects.all()
        role_filter = request.GET.get('role', None)

        if role_filter:
            users = users.filter(role=int(role_filter))

        context = {
            'users': users,
        }
        return render(request, self.template_name, context)

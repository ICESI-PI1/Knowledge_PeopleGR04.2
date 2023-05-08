from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import User



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su correo electrónico'
    }))
    name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su nombre'
    }))
    
    TI=1
    CC=2
    CE=3
    NIT=4

    id_type_choices = [(TI,'Tarjeta de Identidad'),
            (CC,'Cédula de Ciudadanía'),
            ( CE,'Cédula extranjera'),
            (NIT,'NIT')]
    
    idType = forms.ChoiceField(label='Tipo de identificación', widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=id_type_choices)
    numID = forms.CharField(label='Número de identificación', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su número de identificación'
    }))

    BENEFICIARY=1
    DONOR=2
    INSTITUTION=3
    role_choices =[(BENEFICIARY, 'Beneficiario'),
            (DONOR,'Donante'),
            (INSTITUTION,'Institución')]

    role = forms.ChoiceField(label='Registrarse como', widget=forms.Select(attrs={
        'class': 'form-control'
    }), choices=role_choices) 

    profilePicture = forms.ImageField(label='Foto de perfil', widget=forms.FileInput(attrs={
        'class': 'form-control'
    }), required=False)

    password1 = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Crea una contraseña',
        'autocomplete': 'current-password',
    }))

    password2 = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirma tu contraseña',
        'autocomplete': 'current-password',
    }))

    class Meta:
        model = User
        fields = ("email","name","idType", 'numID', 'role','profilePicture')
        labels = {
            "email": "Correo electrónico",
            "name": "Nombre",
            "idType": "Tipo de identificación",
            "numID": "Número de identificación",
            "role": "Registrarse como",
            "profilePicture": "Foto de perfíl"
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email", )

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Correo electrónico',
    }))
    password = forms.CharField(label='Contraseña', strip=False, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Contraseña',
        'autocomplete': 'current-password',
    }))
    
    error_messages = {
        'invalid_login': 'Correo electrónico o contraseña incorrectos',
        'inactive': 'Esta cuenta no está activa.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Correo electrónico',
            'class': 'form-control',
        })
        self.fields['password'].label = ''
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Contraseña',
            'class': 'form-control',
        })
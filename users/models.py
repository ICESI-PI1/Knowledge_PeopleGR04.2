from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username=None
    BENEFICIARY=1
    DONOR=2
    INSTITUTION=3

    ROLE_CHOICE=(
          (BENEFICIARY, 'Beneficiario'),
          (DONOR,'Donante'),
          (INSTITUTION,'Institución'),
    )

    TI=1
    CC=2
    CE=3
    NIT=4

    IDTYPE_CHOICE= ((TI,'Tarjeta de Identidad'),
                (CC,'Cédula de Ciudadanía'),
                ( CE,'Cédula extranjera'),
                (NIT,'NIT'))
    email = models.EmailField(_("email address"), unique=True)
    name=models.CharField(max_length=100,null=False)
    profilePicture= models.ImageField(upload_to="users",null=True, blank=True)
    idType = models.PositiveSmallIntegerField(choices=IDTYPE_CHOICE,null=False)
    numID = models.CharField(max_length=10,null=False)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,null=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
   
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'idType', 'numID', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email
     
    def has_module_perms(self, app_label):
       return self.is_superuser
    def has_perm(self, perm, obj=None):
       return self.is_superuser
    

class Donor(User):
    pass

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Donor'

class Beneficiary(User):
    # beneficiary specific fields
    birth_date = models.DateField()
    optionsGender = (('F','Femenino'),
                     ('M','Masculino'),
                     ('O','Otro'))
    gender = models.CharField(max_length=15,choices=optionsGender,null=False) 

    def __str__(self):
        return self.name + " " + self.email    
    
    class Meta:
        verbose_name = 'Beneficiary'
        verbose_name_plural = 'Beneficiaries'


class Institution(User):
    optionsInstitution = (('Tecnicas','Tecnicas'),
                              ('Tecnologas','Tecnologas'),
                                   ('Universitaria','Universitaria'))
     
    type_institution = models.CharField(max_length=200,choices=optionsInstitution,null=False)
    location = models.CharField(max_length=70)
    money_donation = models.IntegerField(default=0)

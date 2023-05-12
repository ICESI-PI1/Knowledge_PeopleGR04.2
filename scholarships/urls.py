from django.urls import path
from users.views import BeneficiaryUpdateView
from . import views

app_name = 'scholarships'

urlpatterns = [path("showmenu/", views.ShowMenu.as_view(), name="showmenu"), 
               path("newapplication/", views.NewApplication.as_view(), name="newapplication"),
               path("insertScholarship/", views.InsertScholarship.as_view(), name="insertScolarship"),
                path('beneficiaries/<int:pk>/update/', views.BeneficiaryUpdateView.as_view(), name='beneficiary_profile_update'),
                path('naturaldonor/<int:pk>/update/', views.NaturalDonorUpdateView.as_view(), name='natural_donor_profile_update'),
                path('legaldonor/<int:pk>/update/', views.LegalDonorUpdateView.as_view(), name='legal_donor_profile_update'),
                path('institution/<int:pk>/update/', views.InstitutionUpdateView.as_view(), name='institution_profile_update'),
            ]
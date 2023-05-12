from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [path("signupBen/", views.SignUpBen.as_view(), name="signupb"), 
               path("signupDon/", views.SignUpDon.as_view(), name="signupd"), 
               path("sigin/", views.SigIn.as_view(),name="sigin"), 
                path('beneficiaries/<int:pk>/update/', views.BeneficiaryUpdateView.as_view(), name='beneficiary_update'),
                path('naturaldonors/<int:pk>/update/', views.NaturalDonorUpdateView.as_view(), name='natural_donor_update'),
                path('legaldonors/<int:pk>/update/', views.LegalDonorUpdateView.as_view(), name='legal_donor_update'),
                path('institutions/<int:pk>/update/', views.InstitutionUpdateView.as_view(), name='institution_update'),]   
                
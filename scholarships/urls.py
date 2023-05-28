from django.urls import path
from users.views import BeneficiaryUpdateView
from . import views
from.views import NewDonation

app_name = 'scholarships'

urlpatterns = [path("showmenu/", views.ShowMenu.as_view(), name="showmenu"), 
               path("newapplication/", views.NewApplication.as_view(), name="newapplication"),
               path("lookapplications/", views.LookApplication.as_view(), name="lookapplication"),
               path("insertScholarship/", views.InsertScholarship.as_view(), name="insertScolarship"),
                path('beneficiaries/<int:pk>/update/', views.BeneficiaryUpdateView.as_view(), name='beneficiary_profile_update'),
                path('naturaldonor/<int:pk>/update/', views.NaturalDonorUpdateView.as_view(), name='natural_donor_profile_update'),
                path('legaldonor/<int:pk>/update/', views.LegalDonorUpdateView.as_view(), name='legal_donor_profile_update'),
                path('institution/<int:pk>/update/', views.InstitutionUpdateView.as_view(), name='institution_profile_update'),
                path("soli_Activa/", views.ActiveSolicitud.as_view(), name="soli_Activa"),
                path("editSolicitudActiva/", views.EditSolicitud.as_view(), name='editSolicitudActiva'),
                path("newdonation/", NewDonation.as_view(), name='newdonation')
            ]
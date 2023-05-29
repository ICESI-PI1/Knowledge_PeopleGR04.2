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
                path("newdonation/", NewDonation.as_view(), name='newdonation'),
                path("lookbeneficiaries/", views.LookBeneficiaries.as_view(), name='look_beneficiaries'),
                path("lookInstitutios/", views.LookInstitutions.as_view(), name='look_institutions'),
                path("filtersemester/<int:id>/'", views.FilterSemester.as_view(), name='filtersemester'),
                path("filterinstitution/<int:id>/'", views.FilterInstitution.as_view(), name='filterinstitution'),
                path("filterprogram/<str:program_name>/'", views.FilterProgram.as_view(), name='filterprogram'),
                path('filtervalue/<int:min_value>/<int:max_value>/', views.FilterInterval.as_view(), name='filtervalue'),
                path('showdetailsBen/<int:id>/', views.ShowDetailsBen.as_view(), name='showdetailsbeneficiary'),
 ]
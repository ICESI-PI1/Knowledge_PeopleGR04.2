from django.urls import path
from . import views


urlpatterns = [path("signupBen/", views.SignUpBen.as_view(), name="signupb"), 
               path("signupDon/", views.SignUpDon.as_view(), name="signupd"), 
               path("sigin/", views.SigIn.as_view(),name="sigin"),]
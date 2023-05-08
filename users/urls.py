from django.urls import path
from . import views


urlpatterns = [path("signup/", views.SignUp.as_view(), name="signup"), 
               path("sigin/", views.SigIn.as_view(),name="sigin"),]
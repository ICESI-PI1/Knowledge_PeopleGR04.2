from django.urls import path
from . import views

app_name = 'scholarships'

urlpatterns = [path("showmenu/", views.ShowMenu.as_view(), name="showmenu"), 
               ]
from django.urls import path
from . import views

app_name = 'scholarships'

urlpatterns = [path("showmenu/", views.ShowMenu.as_view(), name="showmenu"), 
               path("newapplication/", views.NewApplication.as_view(), name="newapplication"),
               path("insertScholarship/", views.InsertScholarship.as_view(), name="insertScolarship"),
               ]
from django.urls import path
  
from . import views

urlpatterns =[
             path('<str:UID>/edit/',views.edit_squirrel),
             ]

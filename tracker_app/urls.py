from django.urls import path
  
from . import views

urlpatterns =[
             path('sightings/<str:UID>/',views.edit_squirrel),
             path('sightings/add/',views.add_squirrel),
             path('map/',views.map_squirrel),
             path('sightings/',views.sighting),
             ]

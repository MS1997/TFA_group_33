from django.urls import path
  
from . import views

urlpatterns =[
             path('<str:UID>/edit/',views.edit_squirrel),
             path('sightings/add',views.add_squirrel),
             path('map/',views.map_squirrel),
             path('sightings/',views.sighting),
             ]

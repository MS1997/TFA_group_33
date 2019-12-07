from django.urls import path
  
from . import views

urlpatterns =[
             path('sightings/<str:UID>',views.edit_squirrel),
             path('sightings/add/',views.add_squirrel),
             path('sightings/stats/',views.get_stats),
             path('sightings/',views.sighting),
             path('map/', views.map_squirrel),
             ]

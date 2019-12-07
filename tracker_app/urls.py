from django.urls import path
  
from . import views

urlpatterns =[
<<<<<<< HEAD
             path('sightings/<str:UID>',views.edit_squirrel),
             path('sightings/add/',views.add_squirrel),
             path('sightings/stats/',views.get_stats),
=======
             path('sightings/<str:UID>/',views.edit_squirrel),
             path('sightings/add/',views.add_squirrel),
>>>>>>> 2bbb717e1f5bf24e732d883cf23b4b0ce995b347
             path('map/',views.map_squirrel),
             path('sightings/',views.sighting),
             ]

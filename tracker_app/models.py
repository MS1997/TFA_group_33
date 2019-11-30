 from django.db import models
  
 from django.utils.translation import gettext as _
 
 class squirrel(models.Model):
     X = models.FloatField(
         max_length=100,
         help_text=_('Longitide Coordinate for Squirrel sighting point'),
                            


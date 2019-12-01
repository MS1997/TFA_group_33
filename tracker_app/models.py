from django.db import models

from django.utils.translation import gettext as _
                                                                          class squirrel(models.Model):
     X = models.FloatField(
         max_length=100,
         help_text=_('Longitude Coordinate for Squirrel sighting point'),
         )
     Y = models.FloatField(
         max_length=100,
         help_text=_('Latitude Coordinate for Squirrel sighting point'),
         )
     UID = models.CharField(
         max_length=100,
         help_text=_('Identification tag for Squirrel sighting'),
         )
     SHIFT_CHOICES =(
            (AM,'AM'),
            (PM,'PM'),
            )
     Shift  = models.CharField(
         max_length=100,
         choices = SHIFT_CHOICES,
         help_text=_('Squirrel sighting session morning or late afternoon'),
         )
     Date = models.DateField(
         max_length=100,
         help_text=_('Session of sighting day and month'),
         )
     AGE_CHOICES = (
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            ) 
     Age = models.CharField(
         max_length=100,
         choices = AGE_CHOICES,
         help_text=_('Value is either adult or juvenile'),
         )
    COLOR_CHOICES = ((GREY,'Grey'),
            (CINNAMON,'Cinnamon'),
            (BLACK,'Black'),
            )
    Primary_Fur_Color = models.CharField(
            max_length=100,
            blank=True,
            help_text=_('fur color of squirrel'),
    )
    LOCATION_CHOICES =(
            (GROUND_PLANE,'Ground Plane'),
            (ABOVE_GROUND,'Above Ground'),
            )
    Location = models.CharField(
            max_length=50,
            choices = LOCATION_CHOICES,
            blank=True,
            help_text=_('sighter instructed squirrel location'),
    )
    Specific_Location = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('sighter commentary on  squirrel location'),
    )
    Running = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen running'),
            )
    Chasing = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen chasing'),
            )
    Climbing = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen climbing'),
            )
    Eating = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen eating'),
            )
    Foraging = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen foraging for food'),
            )
    Other_activities = models.CharField(
            max_length=200,
            blank=True,
            help_text=_('no description available '),
    )
    Kuks = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was heard kukking, a chirpy vocal communication'),
            )
    Quaas = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was heard quaaing, an elongated vocal communication'),
            )
    Moans = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was heard moaning, a high-pitched vocal communication'),
            )
    Tail_flags = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen flagging its tail'),
            )
    Tail_twitches = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen twitching its tail'),
            )
    Approaches = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen approaching human, seeking food')
            )
    Indifferent = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was indifferent to human presence'),
            )
    Runs_From = models.BooleanField(
            max_length = 10,
            help_text=_('Squirrel was seen running from humans, seeing them as a threat'),
            )

import csv
from django.db import IntegrityError
from django.core.management import BaseCommand
from tracker.models import Squirrel
import argparse

class Command(BaseCommand):
        help = 'Load a csv file into the database'
            
        def add_arguments(self,parser):
            parser.add_argument('path', type=str)

        def handle(self, *args, **kwargs):
            print('Deleting all sightings..')
            Squirrel.objects.all().delete()
            print('Importing..');
            path = kwargs['path']
            with open(path, 'rt') as f:
                reader = csv.reader(f, dialect='excel')
                next(reader,None)
                for row in reader:
                    squirrel = Squirrel.objects.create(
                            X=row[0],
                            Y=row[1],
                            UID=row[2],
                            Shift=row[4],
                            Date=row[5],
                            Age=row[7],
                            Primary_Fur_Color=row[8],
                            Location=row[12],
                            Specific_Location=row[14],
                            Running=(row[15]=='true'),
                            Chasing=(row[16]=='true'),
                            Climbing=(row[17]=='true'),
                            Eating=(row[18]=='true'),
                            Foraging=(row[19]=='true'),
                            Other_activities=row[20],
                            Kuks=(row[21]=='true'),
                            Quaas=(row[22]=='true'),
                            Moans=(row[23]=='true'),
                            Tail_flags=(row[24]=='true'),
                            Tail_twitches=(row[25]=='true'),
                            Approaches=(row[26]=='true'),
                            Indifferent=(row[27]=='true'),
                            Runs_From=(row[28] == 'true'),
                          )
                    squirrel.save()
                except IntegrityError as e:
                print('Skipping', row[2], 'due to integrity error') 


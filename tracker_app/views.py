from django.http import HttpResponse
from django.shortcuts import render,redirect
  
from .models import Squirrel
from .forms import SquirrelForm

# Create your views here.
def edit_squirrel(request,UID):
    squirrel= Squirrel.objects.get(UID=UID)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm(instance=squirrel)
    context ={
            'form':form,
             }
    return render(request, 'tracker_app/edit.html', context)

def add_squirrel(request):
    if request.method == "POST":
        form= SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
    context ={
            'form':form,
        }
    return render(request,'tracker_app/edit.html',context)

def map_squirrel(request):
    sightings= Squirrel.objects.all()[:100]
    context ={
            'sightings':sightings,
             }
    return render(request, 'tracker_app/map.html', context)

def sighting(request):
    squirrel = Squirrel.objects.all()
    context = {
            'squirrels': squirrel,
        }
    return render(request, 'tracker_app/sightings.html',context)

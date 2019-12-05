from django.shortcuts import redirect
  
from .models import Squirrel
from .forms import SquirrelForm

# Create your views here.
def edit_squirrel(request,UID):
    squirrel= Squirrel.objects.get(id=UID)
    if request.method =='POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/tracker_app/{UID}')
    else:
        form = SquirelForm(instance=squirrel)
    context ={
            'form':form,
             }
    return render(request, 'tracker_app/edit.html', context)

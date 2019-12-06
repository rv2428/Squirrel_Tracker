from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels
from .forms import SquirrelForm

def index(request):
    context = {"sightings": Squirrels.objects.all(), "field_names": Squirrels._meta.get_fields()}
    return render(request, 'Squirrel_Sightings/index.html',context)

def coordinates(request):
    squirrels  = Squirrels.objects.all()[:100]
    context = {
            "squirrels": squirrels,
         }
    return render(request, 'Squirrel_Sightings/map.html', context)

def edit_squirrel(request, Unique_Squirrel_Id):
    squirrel = Squirrels.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel_Sightings/edit.html',context)
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
            'form':form,
        }
    return render(request, 'Squirrel_Sightings/edit.html', context)
def add_squirrel(request):
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel_Sightings/list/')
    else:
        form = SquirrelForm()
    context = {
            'form':form,
        }
    return render(request, '/Squirrel_Sightings/edit.html', context)

from django.shortcuts import render, redirect
from .forms import *
from .models import *

def Home(request):
    return render(request, 'index.html')

def crearActor(request):
    if request.method == 'POST':
        actor_form = ActorForm(request.POST)
        if actor_form.is_valid():
            actor_form.save()
            return  redirect('index')
    else:
        actor_form =ActorForm()
    return render(request, 'sakila/crear_actor.html', {'actor_form':actor_form})

def listarActor(request):
    actores = Actor.objects.all()
    return render(request, 'sakila/listar_actor.html',{'actores':actores})
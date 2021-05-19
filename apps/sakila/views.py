from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *

def Home(request):
    return render(request, 'index.html')

def crearActor(request):
    if request.method == 'POST':
        actor_form = ActorForm(request.POST)
        if actor_form.is_valid():
            actor_form.save()
            return  redirect('/sakila/resultados_busqueda')
    else:
        actor_form =ActorForm()
    return render(request, 'sakila/crear_actor.html', {'actor_form':actor_form})

def listarActor(request):
    actores = Actor.objects.all()
    return render(request, 'sakila/listar_actor.html',{'actores':actores})

def editarActor(request, actor_id):
        actor = Actor.objects.get(actor_id = actor_id)
        if request.method == 'GET':
            actor_form = ActorForm(instance = actor)
        else:
            actor_form =ActorForm(request.POST, instance = actor)
            if actor_form.is_valid():
                actor_form.save()
            return redirect('sakila:resultados_busqueda')

        return render(request,'sakila/crear_actor.html',{'actor_form':actor_form})

def eliminarActor (request, actor_id):
    actor = Actor.objects.get(actor_id = actor_id)
    actor.delete()
    return redirect('sakila:resultados_busqueda')

def filtrarActores(request):
    if 'prd' in request.GET != None:
        prd= request.GET['prd']
        actores=Actor.objects.filter(first_name=prd)
        return render(request, 'sakila/resultados_busqueda.html', {'actores': actores})
    else:
        actores = Actor.objects.all()
        return render(request, 'sakila/resultados_busqueda.html', {'actores': actores })
def buscar(request):
    if 'prd' in request.GET:
        prd= request.GET['prd']
        actores=Actor.objects.filter(first_name=prd)
        return render(request, 'sakila/resultados_busqueda.html', {'actores': actores})
    else:
        actores = Actor.objects.all()
        return render(request, 'sakila/resultados_busqueda.html', {'actores': actores })
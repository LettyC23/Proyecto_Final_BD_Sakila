from django.urls import path

from apps.sakila.views import crearActor, listarActor

urlpatterns = [
    path('crear_actor/', crearActor, name = 'crear_actor'),
    path('listar_actor/', listarActor, name = 'listar_actor')
]
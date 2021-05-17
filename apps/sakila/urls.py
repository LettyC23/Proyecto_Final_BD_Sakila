from django.urls import path
from apps.sakila.views import *

urlpatterns = [
    path('crear_actor/', crearActor, name = 'crear_actor'),
    path('listar_actor/', listarActor, name = 'listar_actor'),
    path('editar_actor/<int:actor_id>', editarActor, name = 'editar_actor'),
    path('eliminar_actor/<int:actor_id>', eliminarActor, name = 'eliminar_actor')
]
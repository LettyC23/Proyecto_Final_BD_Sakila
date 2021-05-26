from django.urls import path
from apps.sakila.views import *
from apps.sakila import views

urlpatterns = [
    path('crear_actor/', crearActor, name = 'crear_actor'),
    path('resultados_busqueda/', listarActor, name = 'listar_actor'),
    path('editar_actor/<int:actor_id>', editarActor, name = 'editar_actor'),
    path('eliminar_actor/<int:actor_id>', eliminarActor, name = 'eliminar_actor'),
    path('buscar_actor/', filtrarActores, name = 'buscar_actor'),
    path('listar_actor/', buscar, name = 'buscar'),
    path('resultados_busqueda/', buscar, name = 'resultados_busqueda'),
    path('listar_actores/', views.ListActoresPdf.as_view(), name = 'actores_all'),

]
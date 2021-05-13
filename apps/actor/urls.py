from django.urls import path

from apps.actor.views import crearActor

urlpatterns = [
    path('crear_actor/', crearActor, name = 'crear_actor')
]
from django.urls import path
from .views import crearActor


urlpatterns = [
path('crear_actor/', crearActor, name = 'crear_actor')
]
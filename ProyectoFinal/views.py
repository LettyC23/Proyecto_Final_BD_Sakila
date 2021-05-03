from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
from django.views.generic import TemplateView, ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'



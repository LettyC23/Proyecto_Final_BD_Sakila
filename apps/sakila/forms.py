from django import forms
from .models import *
import django_filters


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name', 'last_name']


class AutorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['first_name','last_name']
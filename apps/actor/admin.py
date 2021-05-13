from django.contrib import admin
from .models import *

@admin.register(Actor)
#@admin.register(Country)
class SettingsAdmin(admin.ModelAdmin):
    pass
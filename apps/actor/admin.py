from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class Actor(admin.ModelAdmin):
    pass
#admin.site.register(Actor)

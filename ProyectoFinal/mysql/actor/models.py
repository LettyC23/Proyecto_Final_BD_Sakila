from django.db import models

class Actor(models.Model):
    first_name = models.CharField(blank=True, max_length=45, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=45, verbose_name='last name')
    last_update = models.DateTimeField(blank=True, max_length=45, verbose_name='last update')

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Actor'
        verbose_name_plural = 'Actores'

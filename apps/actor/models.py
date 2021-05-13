from django.db import models


class Actor(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=False, null=False)
    last_name = models.CharField(max_length=45, blank=False, null=False)
    last_update = models.DateTimeField(max_length=45, blank=False, null=False)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actores'
        ordering = ['first_name']

    def __str__(self):
        return self.first_name


from django.db import models

class SingletonModel(models.Model):
    def save (self, *args, **kwargs):
        self.object.pk = 1
        super().save(*args, **kwargs)

class Actor(SingletonModel):
    actor_id = models.AutoField(primary_key = True)
    first_name = models.CharField(blank=True, max_length=45, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=45, verbose_name='last name')
    last_update = models.DateTimeField(blank=True, max_length=45, verbose_name='last update')

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Actor'
        verbose_name_plural = 'Actores'

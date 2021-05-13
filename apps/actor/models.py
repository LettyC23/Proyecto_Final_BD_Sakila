from django.db import models


class SingletonModel(models.Model):
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Actor(SingletonModel):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=False, null=False)
    last_name = models.CharField(max_length=45, blank=False, null=False)
    last_update = models.CharField(max_length=5, blank=False, null=False)


class Country(SingletonModel):
    country_id = models.AutoField(primary_key=True)
    last_update = models.TimeField(max_length=45, blank=False, null=False)

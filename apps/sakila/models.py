from django.db import models

class Actor(models.Model):

    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=False, null=False)
    last_name = models.CharField(max_length=45, blank=False, null=False)
    last_update = models.CharField(max_length=45, blank=False, null=False)

    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'

    def __str__(self):
        return self.first_name

class Country(models.Model):

    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50, blank=False, null=False)
    last_update = models.CharField(max_length=45, blank=False, null=False)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50, blank=False, null=False)
    country_id = models.CharField(max_length=50, blank=False, null=False)
    last_update = models.CharField(max_length=45, blank=False, null=False)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city
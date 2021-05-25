from django.db import models

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    last_update = models.DateTimeField(auto_now=True)



class Country(models.Model):
    country_id = models.AutoField( primary_key=True)
    country = models.CharField(max_length=50,  null=False)
    last_update = models.CharField(max_length=45,  null=False)



class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50, null=False)
    country_id = models.CharField(max_length=50, null=False)
    last_update = models.CharField(max_length=45, null=False)


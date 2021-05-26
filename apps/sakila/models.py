from django.core.validators import RegexValidator
from django.db import models

class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    name_regex = RegexValidator(regex=r'^[a-zA-Z]+$', message="Debes ingresar sólo letras!!")
    first_name = models.CharField(max_length=45, null=False, validators=[name_regex])
    last_name = models.CharField(max_length=45, null=False, validators=[name_regex])
    last_update = models.DateTimeField(auto_now=True)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField(auto_now=True)
    films = models.ManyToManyField('Film', through='FilmCategory')

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    City = models.CharField(max_length=50, null=False)
    country_id = models.CharField(max_length=50, null=False)
    last_update = models.CharField(max_length=45, null=False)

class Country(models.Model):
    country_id = models.AutoField( primary_key=True)
    country = models.CharField(max_length=50,  null=False)
    last_update = models.CharField(max_length=45,  null=False)


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, blank=True)
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    picture = models.BinaryField(blank=True, null=True)


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey(
        Staff,  on_delete=models.CASCADE
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(auto_now=True)
    active = models.IntegerField(blank=True, null=True)


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)
    special_features = models.TextField(blank=True)
    fulltext = models.TextField()
    categories = models.ManyToManyField(Category, through='FilmCategory')
    actors = models.ManyToManyField(Actor, through='FilmActor')


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)



class FilmActor(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class FilmCategory(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff,  on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)





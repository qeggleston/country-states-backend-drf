from django.db import models

# Create your models here.
class Country(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)

class State(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

class City(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
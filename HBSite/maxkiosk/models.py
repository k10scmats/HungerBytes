from django.db import models

# Create your models here.

class User(models.Model):
    pass_id = models.BigIntegerField(primary_key=True, help_text="Serial number from hop pass (7 bytes)")
    gender = models.IntegerField(choices=enumerate(["M", "F", "X"]), blank=True)
    #orientation = models...
    birthdate = models.DateField(blank=True)
    guardian = models.BooleanField(blank=True)
    limited_mobility = models.BooleanField(blank=True)
    #favored locations
    #education/skillset

class Service(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    phone = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    type = models.SmallIntegerField(choices=enumerate(["Shelters", "Basic Needs", "Food and Meals", "Healthcare", "Transportation"]))
# Shelters
# Basic Needs
# Food / Meals
# Health Care
# Transportation

class Kiosk(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    type = models.SmallIntegerField(choices=enumerate(["Hop", "Max", "Bus Stop", "Plate Park", "NikeBike", "PDX Park"]))
    
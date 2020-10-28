from django.db import models


class Departure(models.Model):
    shortname = models.CharField(max_length=10)
    fullname = models.CharField(max_length=64)


class Tour(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    departure = models.ForeignKey(Departure, on_delete=models.CASCADE())
    picture = models.TextField()
    price = models.IntegerField()
    stars = models.IntegerField()
    country = models.CharField(max_length=64)
    nights = models.IntegerField()
    date = models.DateField()

from django.db import models

class Metrics(models.Model):
    id = models.CharField(primary_key=True, null=False, max_length=10)
    metrics = models.CharField(max_length=50)

class Locations(models.Model):
    id = models.CharField(primary_key=True, null=False, max_length=10)
    location = models.CharField(max_length=50)

class WeatherData(models.Model):
    value = models.DecimalField(max_digits=5,decimal_places=2)
    year = models.IntegerField()
    month = models.IntegerField()
    metrics = models.ForeignKey(Metrics, default = 1, related_name='metrics_id', on_delete = models.SET_DEFAULT)
    location = models.ForeignKey(Locations, default = 1,related_name='location_id', on_delete = models.SET_DEFAULT)
    # Create your models here.

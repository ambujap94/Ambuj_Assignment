from django.db import models

class Metrics(models.Model):
    metric = models.CharField(max_length=50, primary_key=True)

class Locations(models.Model):
    location = models.CharField(max_length=30, primary_key=True)

class WeatherData(models.Model):
    class Meta:
        unique_together = (('year','month','location','metric'), )

    value = models.DecimalField(max_digits=10,decimal_places=4)
    year = models.IntegerField()
    month = models.IntegerField()
    metric = models.ForeignKey(
        Metrics,
        on_delete = models.CASCADE,
    )
    location = models.ForeignKey(
        Locations,
        on_delete = models.CASCADE
    )

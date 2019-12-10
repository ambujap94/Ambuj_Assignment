from django.db import models

class Metrics(models.Model):
    metric = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.metric

class Locations(models.Model):
    location = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.location

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
    # metrics = models.ForeignKey(Metrics, default = 1, related_name='metrics_id', on_delete = models.SET_DEFAULT)
    # location = models.ForeignKey(Locations, default = 1,related_name='location_id', on_delete = models.SET_DEFAULT)
    # Create your models here.

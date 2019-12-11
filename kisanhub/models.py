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
        unique_together = (('date','location','metric'), )
        ordering = ['date']

    value = models.DecimalField(max_digits=10,decimal_places=4)
    date = models.DateField()
    metric = models.ForeignKey(
        Metrics,
        on_delete = models.CASCADE,
    )
    location = models.ForeignKey(
        Locations,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return f"WeatherData({self.date})"
    
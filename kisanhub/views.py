from django.shortcuts import render
from kisanhub.models import WeatherData, Metrics, Locations
from rest_framework import generics
from kisanhub.serializers import WeatherDataSerializer, MtericsSerializer, LocationSerializer

# Create your views here.
class MetricsView(generics.CreateAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MtericsSerializer


class LocationsView(generics.CreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer


class WeatherDataView(generics.CreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer



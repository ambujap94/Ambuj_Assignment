from django.shortcuts import render
from kisanhub.models import WeatherData, Metrics, Locations
from rest_framework import generics
from kisanhub.serializers import WeatherDataSerializer, MetricsSerializer, LocationSerializer

# Create your views here.
class MetricsView(generics.CreateAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer


class LocationsView(generics.CreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer


class WeatherDataView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

    # def post(self, validated_data):
    #     print("HAHA")
    #     location = validated_data.pop('location')
    #     print(location)
    #     location = Location.objects.get(name=location.get('name'))
    #     print(location)
    #     metric = validated_data.pop('metric')
    #     print(metric)
    #     metric = Metric.objects.get(name=metric.get('name'))
    #     print(metric)
    #     WeatherData.objects.create(**validated_data, location=location, metric=metric)

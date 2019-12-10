from django.shortcuts import render
from kisanhub.models import WeatherData, Metrics, Locations
from rest_framework import generics
from kisanhub.serializers import WeatherDataSerializer, MetricsSerializer, LocationSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class MetricsView(generics.ListCreateAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer


class LocationsView(generics.ListCreateAPIView):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer


class WeatherDataView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['metric','location']
    #ordering_fields = ['year', 'month']
    
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

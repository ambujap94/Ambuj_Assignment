from django.shortcuts import render
from kisanhub.models import WeatherData, Metric, Location
from rest_framework import generics, status
from rest_framework.response import Response
from kisanhub.serializers import WeatherDataSerializer, MetricSerializer, LocationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import WeatherDataFilter

# Create your views here.
class MetricView(generics.ListCreateAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer


class LocationView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class WeatherDataView(generics.ListCreateAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WeatherDataFilter
    ordering_fields = ['date']
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        is_many = isinstance(request.data, list)
        if is_many:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return super().post(request, *args, **kwargs)
        
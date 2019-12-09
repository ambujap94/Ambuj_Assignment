from kisanhub.models import WeatherData, Metrics, Locations
from rest_framework import serializers


class MtericsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = ['id', 'metrics']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['id', 'location']


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['value', 'year', 'month','metrics_id','location_id']

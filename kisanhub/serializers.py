from kisanhub.models import WeatherData, Metrics, Locations
from rest_framework import serializers


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = ['metric']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['location']
    

class WeatherDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WeatherData
        extra_kwargs = {'metric': {'write_only': True, },
                        'location': {'write_only': True, }}
        fields = ['value', 'year', 'month', 'metric', 'location']

print(repr(WeatherDataSerializer()))
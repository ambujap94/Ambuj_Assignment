from kisanhub.models import WeatherData, Metrics, Locations
from rest_framework import serializers


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = ['metric']

    def create(self, validated_data):
        print(validated_data)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['location']

    def create(self, validated_data):
        print(validated_data)


class WeatherDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WeatherData
        extra_kwargs = {'metric': {'write_only': True, },
                        'location': {'write_only': True, }}
        fields = ['value', 'year', 'month', 'metric', 'location']
       
    
print(repr(WeatherDataSerializer()))
    
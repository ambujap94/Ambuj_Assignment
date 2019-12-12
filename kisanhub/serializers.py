from kisanhub.models import WeatherData, Metric, Location
from rest_framework import serializers
import datetime
from django.utils import timezone


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ['metric']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location']

    
class WeatherDataSerializer(serializers.ModelSerializer):
    value = serializers.FloatField()
    month = serializers.IntegerField(source = 'date.month')
    year = serializers.IntegerField(source = 'date.year')

    
    class Meta:
        model = WeatherData
        extra_kwargs = {'metric': {'write_only': True, },
                        'location': {'write_only': True, }}
        fields = ['value', 'year', 'month', 'metric', 'location']

    def create(self, validated_data):
        date = validated_data.pop('date')
        date = datetime.date(**date, day=1)
        return WeatherData.objects.create(**validated_data, date = date)
       
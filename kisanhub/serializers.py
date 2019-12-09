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
    # metric = MetricsSerializer(write_only=True) # serializers.ModelField(MetricsSerializer, source = 'weather_data.metric', write_only=True)
    # location = LocationSerializer(write_only=True) # serializers.ModelField(LocationSerializer, source='weather_data.location', write_only=True)
    class Meta:
        model = WeatherData
        fields = ['value', 'year', 'month', 'metric', 'location']
        #write_only_fields = ('metric', 'location')

    def validate(self, data):
        print(data)

    def validate_location(self, value):
        print("YAHA")
        location = Locations.objects.get(name=value)
        return location.id

    def validate_metric(self, value):
        print("WAHA")
        metric = Metrics.objects.get(name=value)
        return metric.id

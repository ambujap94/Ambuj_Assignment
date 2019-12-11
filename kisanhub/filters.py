from django_filters import rest_framework as filters
from .models import WeatherData

class WeatherDataFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name = 'date', lookup_expr = 'gte', label = 'Start Date (MM/dd/yyyy)')
    end_date = filters.DateFilter(field_name = 'date', lookup_expr = 'lte',  label = 'End Date (MM/dd/yyyy)')

    class Meta:
        model = WeatherData
        fields = ['start_date','end_date','metric','location']
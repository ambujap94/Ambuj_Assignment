from django.urls import path
from kisanhub.views import WeatherDataView, MetricView, LocationView

app_name="kisanhub"
urlpatterns = [
    path('weatherdata', WeatherDataView.as_view(), name="weatherdata"),
    path('metric', MetricView.as_view(), name="metric"),
    path('location', LocationView.as_view(), name="location")
]
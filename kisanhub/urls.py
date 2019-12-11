from django.urls import path
from kisanhub.views import WeatherDataView, MetricsView, LocationsView

app_name="kisanhub"
urlpatterns = [
    path('weatherdata', WeatherDataView.as_view(), name="weatherdata"),
    path('metric', MetricsView.as_view(), name="metric"),
    path('location', LocationsView.as_view(), name="location")
]
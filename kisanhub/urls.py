from django.urls import path
from kisanhub.views import WeatherDataView, MetricsView, LocationsView

urlpatterns = [
    path('weatherdata', WeatherDataView.as_view()),
    path('metric', MetricsView.as_view()),
    path('location', LocationsView.as_view())
]
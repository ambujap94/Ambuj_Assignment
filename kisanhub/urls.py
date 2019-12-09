from django.urls import path
from kisanhub.views import WeatherDataView, MetricsView, LocationsView

urlpatterns = [
    path('postweatherdata', WeatherDataView.as_view()),
    path('addmetrics', MetricsView.as_view()),
    path('addlocation', LocationsView.as_view())
]
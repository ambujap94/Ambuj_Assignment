from rest_framework.test import APITestCase
from kisanhub.models import WeatherData, Metrics, Locations
from django.urls import reverse
import datetime

class WeatherDataAPITestCase(APITestCase):

    def setUp(self):
        
        WeatherData.objects.create(value = 45.2,
            date = "1500-05-01",
            metric = Metrics.objects.create(metric="Rainfall"),
            location = Locations.objects.create(location="England"))

    def test_get_method(self):
        endpoint = reverse("kisanhub:weatherdata")
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code,200)
        qs=WeatherData.objects.filter(metric="Rainfall")
        self.assertEqual(qs.count(),1)

    def test_post_method_success(self):
        endpoint = reverse("kisanhub:weatherdata")
        date = datetime.date(year=2019, month=1, day=1)
        data={
                "value":22.00,
                "year" : date.year,
                "month" : date.month, # 2019 Jan Data
                "metric" : "Rainfall",
                "location" : "England"
            }
        response = self.client.post(endpoint,data,format='json')
        self.assertEqual(response.status_code,201)
        qs = WeatherData.objects.filter(metric="Rainfall", location="England", date=date)
        self.assertEqual(qs.count(),1)

    def test_post_method_failure(self):
        endpoint = reverse("kisanhub:weatherdata")
        date = datetime.date(year=2019, month=1, day=1)
        data={
                "value":22.00,
                "year" : date.year,
                "month" : date.month, # 2019 Jan Data
            }
        response = self.client.post(endpoint,data,format='json')
        self.assertEqual(response.status_code,400)


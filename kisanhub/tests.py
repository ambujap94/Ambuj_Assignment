from rest_framework.test import APITestCase
from kisanhub.models import WeatherData, Metrics, Locations
from django.urls import reverse
import datetime


class WeatherDataAPITestCase(APITestCase):

    def setUp(self):
        metric = Metrics.objects.create(metric="Rainfall")
        location = Locations.objects.create(location="England")
        WeatherData.objects.create(value = 45.2,
            date = "2019-12-01",
            metric = metric,
            location = location)

    def test_get_method(self):
        endpoint = reverse("kisanhub:weatherdata")
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        query_set = WeatherData.objects.filter(metric="Rainfall")
        self.assertEqual(query_set.count(), 1)

    def test_post_method_success(self):
        endpoint = reverse("kisanhub:weatherdata")
        date = datetime.date(year=2019, month=1, day=1)
        data = {
                "value":22.00,
                'year' :date.year,
                'month': date.month, # 2019 Jan data
                "metric" :"Rainfall",
                "location" : "England"
            }
        response = self.client.post(endpoint, data, format='json')
        self.assertEqual(response.status_code, 201)
        query_set = WeatherData.objects.filter(metric="Rainfall", location="England", date=date)
        self.assertEqual(query_set.count(), 1)

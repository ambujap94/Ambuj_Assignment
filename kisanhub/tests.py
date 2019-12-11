from rest_framework.test import APITestCase
from kisanhub.models import WeatherData, Metrics, Locations

class WeatherDataAPITestCase(APITestCase):

    def setUp(self):
        
        WeatherData.objects.create(value = 45.2,
            date = "1500-05-01",
            metric = Metrics.objects.create(metric="Rainfall"),
            location = Locations.objects.create(location="England"))

    def test_get_method(self):
        url = "http://127.0.0.1:8000/weatherdata"
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=WeatherData.objects.filter(metric="Rainfall")
        self.assertEqual(qs.count(),1)

    # def test_post_method_success(self):
    #     url = "http://127.0.0.1:8000/weatherdata/"
    #     data={
    #             "value":22.00,
    #             # 'year' :1448,
    #             # 'month': 5,
    #             "date" : "1588-05-05",
    #             "metric" : Metrics.objects.create(metric="Tmax"),
    #             "Location" : Locations.objects.create(location="UK")
    #         }
    #     response = self.client.post(url,data,format='json')
    #     print(response.status_code)
    #     self.assertEqual(response.status_code,201)


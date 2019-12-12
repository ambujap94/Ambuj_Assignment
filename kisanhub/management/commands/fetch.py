from django.core.management.base import BaseCommand, CommandError
from kisanhub.serializers import WeatherDataSerializer
from kisanhub.models import Metric, Location
import requests
import logging
from django.urls import reverse


class Command(BaseCommand):
    help = 'fetch the weather dat from S3'

    def add_arguments(self, parser):
        parser.add_argument('location', type=str)
        parser.add_argument('metric', type=str)  
        

    def fetch(self, url, params=None):
        try:
            response = requests.get(url, params=params)
        except Exception as ex:
            logging.exception(ex)
        else:
            return response.json()

    def handle(self, *args, **options):
        # PART1 fetch the data
        
        location = options['location']
        metric = options['metric']
        Metric.objects.get_or_create(metric=metric)
        Location.objects.get_or_create(location=location)
        url = f"https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{metric}-{location}.json"
        print("Fetching from S3")
        weather_data_from_s3 = self.fetch(url)
        print("Inserting using API")
        self.insert(weather_data_from_s3, location, metric)
        print("fetching the inserted data using API")
        inserted_weather_data = self.query(location, metric)
        print("comparing the values")
        if self.validate(inserted_weather_data, weather_data_from_s3):
            print("BOTH ARE THE SAME")
        else:
            print("BOTH ARE NOT THE SAME")

    def validate(self, list1, list2):
        return list1 == list2

    def query(self, location, metric):
        url = 'http://localhost:8000' + reverse('kisanhub:weatherdata')
        return self.fetch(url, params={'location': location, 'metric': metric})

    def insert(self, weather_data_list, location, metric):

        data_to_insert = []
        for wd in weather_data_list:
            wd = wd.copy()
            wd['location'] = location
            wd['metric'] = metric
            data_to_insert.append(wd)

        url = 'http://localhost:8000' + reverse('kisanhub:weatherdata')
        try:
            response = requests.post(url, json=data_to_insert)
        except Exception as ex:
            logging.exception(ex)
        else:
            if response.ok:
                return True
            else:
                return False
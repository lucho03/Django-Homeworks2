from django.test import TestCase
from elsys.models import Car
from datetime import datetime

class TestCarModel(TestCase):
    def setUp(self):
        #called when test is started
        Car.objects.create(color="red", made=datetime.now(), brand="audi", description = "red audi", is_electric=False)
        Car.objects.create(color="green", made=datetime.now(), brand="bmw", description = "red bmw")

    def tearDown(self):
        #called after tests were run
        pass

    def test_car_is_red(self):
        assert Car.objects.get(brand="audi").color == "red"

    def test_car_is_green(self):
        assert Car.objects.get(brand="bmw").color == "green"

    def test_car_sound(self):
        assert Car.objects.get(brand="audi").sound_check() == "brum brum"

from unittest.mock import patch

#class ApiHandler:
#    def call_api(self):
#        response = requests.get("url")
#        data = response['data']
#        return data['a'] + 1


#class TestC(TestCase):
#    @patch("requests.get")
#    def test_call_api(self, mocked_requests):
#        mocked_requests.return_value = {'data':{'a': 1}}
#        response = ApiHandler().call_api()
#        assert response == 2

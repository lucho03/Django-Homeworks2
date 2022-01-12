import json
from django.test import TestCase
from requests.api import patch
from api.api_processor import API
from unittest.mock import Mock, patch
import json

class Test(TestCase):
    @patch('requests.post')
    def test_max_temperature(self, mocked_requests):
        data = json.load(open('./api/temperature.json'))
        mocked_requests.return_value.json = Mock(return_value=data)
        assert API.get_max_temperature() == 8
    
    @patch('requests.post')
    def test_min_temperature(self, mocked_requests):
        data = json.load(open('./api/temperature.json'))
        mocked_requests.return_value.json = Mock(return_value=data)
        assert API.get_min_temperature() == 3

    @patch('requests.post')
    def test_avg_temperature(self, mocked_requests):
        data = json.load(open('./api/temperature.json'))
        mocked_requests.return_value.json = Mock(return_value=data)
        assert API.get_avg_temperature() == 5
import requests

URL = 'https://tues2022.proxy.beeceptor.com/my/api/test'

class API:
    @staticmethod
    def get_max_temperature():
        maxT = -100
        data = requests.post(URL).json()
        
        for x in data['data']:
                if x['temperature'] > maxT:
                    maxT = x['temperature']
        
        return maxT
    
    @staticmethod
    def get_min_temperature():
        minT = 100
        data = requests.post(URL).json()
        
        for x in data['data']:
                if x['temperature'] < minT:
                    minT = x['temperature']
        
        return minT

    @staticmethod
    def get_avg_temperature():
        sumT = 0
        numT = 0
        data = requests.post(URL).json()
        
        for x in data['data']:
            sumT += x['temperature']
            numT += 1
                
        return sumT/numT
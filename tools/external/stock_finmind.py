import os
import sys
import json
import requests
from requests.models import Response

class FinMind():
    def __init__(self,token):
        self.url = "https://api.finmindtrade.com/api/v4/data"
        self.token = token
    
    def request_get(self,parameter):
        response = requests.get(url=self.url,params=parameter)
        if response.status_code == requests.codes.ok:
            try:
                data = response.json()
                if data["status"] == 200:
                    return data["data"]
            except Exception as e:
                print(e)
                return None
        else:
            return None

    def all_info(self):
        parameter = {
            "dataset": "TaiwanStockInfo",
            "token": self.token,
            }
        results = self.request_get(parameter)
        return results
    
    def stock_price_get(self,symbol,start_date):
        '''
        start_date : 2021-12-17
        '''
        parameter = {
            "dataset": "TaiwanStockPriceTick",
            "data_id": symbol,
            "start_date": start_date,
            "token": self.token, 
        }
        results = self.request_get(parameter)
        return results

    # def price(self):
    #     '''
    #     取得單日資訊 當日最高最低價
    #     '''
    #     parameter = {
    #         "dataset": "TaiwanStockPrice",
    #         "data_id": "2330",
    #         "start_date": "2021-12-17",
    #         "end_date": "2021-12-18",
    #         "token": self.token
    #     }
    #     results = self.request_get(parameter)
    #     return results


if __name__ == "__main__":
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRlIjoiMjAyMi0wNC0wNiAxNDowMDo0MyIsInVzZXJfaWQiOiJ3ZWlrYWkiLCJpcCI6IjYxLjIxNi4xMzAuOCJ9.sK83eAUbusItPIsOFoR6YAQCD0ALHmVIyB2_y41tuCU"
    data = FinMind(token).stock_price_get('2330','2022-03-28')
    with open (file=os.path.join('sample_data',"20220406_test.json"),mode='w',encoding="UTF-8") as F :
        json.dump(data , F)
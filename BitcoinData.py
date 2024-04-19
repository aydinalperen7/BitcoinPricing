# api key = b1ab10c3-8652-47d7-8e78-b1e855ae23c5
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pprint
import json
import datetime
import pytz
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split
from joblib import dump, load
from pytrends.request import TrendReq
import requests
from pytrends.request import TrendReq as UTrendReq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
# GET_METHOD='get'
# headers = {
#     # 'https://trends.google.com/trends/explore'
# }

# class TrendReq(UTrendReq):
#     def _get_data(self, url, method=GET_METHOD, trim_chars=0, **kwargs):
#         return super()._get_data(url, method=GET_METHOD, trim_chars=trim_chars, headers=headers, **kwargs)

class GetBitcoinData():
    def __init__(self, apiKey):
        self.bitcoinData = {}
        self.apiKey = apiKey

    def coinMarketApiCall(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
        # 'start':'1',
        # 'limit':'5000',
        'symbol':'BTC',
        'convert':'USD'
        }
        headers = {
        'Accepts': 'application/json',
        # 'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c', ## replace with your own api key
        'X-CMC_PRO_API_KEY': self.apiKey,
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            pprint.pprint(data)
            bitcoin_price = data['data']['BTC']['quote']['USD']['price']
            fully_diluted_market_cap = data['data']['BTC']['quote']['USD']['fully_diluted_market_cap']
            market_cap = data['data']['BTC']['quote']['USD']['market_cap']
            market_cap_dominance = data['data']['BTC']['quote']['USD']['market_cap_dominance']
            percent_change_1h = data['data']['BTC']['quote']['USD']['percent_change_1h']
            percent_change_24h = data['data']['BTC']['quote']['USD']['percent_change_24h']
            percent_change_7d = data['data']['BTC']['quote']['USD']['percent_change_7d']
            percent_change_30d = data['data']['BTC']['quote']['USD']['percent_change_30d']
            percent_change_60d = data['data']['BTC']['quote']['USD']['percent_change_60d']
            percent_change_90d = data['data']['BTC']['quote']['USD']['percent_change_90d']
            volume_24h = data['data']['BTC']['quote']['USD']['volume_24h']
            volume_change_24h = data['data']['BTC']['quote']['USD']['volume_change_24h']
            total_supply = data['data']['BTC']['total_supply']
            max_supply = data['data']['BTC']['max_supply']
            circulating_supply = data['data']['BTC']['circulating_supply']
            
            date = datetime.datetime.now()
            UTC_unixTime = datetime.datetime.timestamp(date)
            time = UTC_unixTime
            [numBuys, numSells] = self.getTradingView()
            # date = datetime.datetime.now()
            current_date = datetime.date.today()
            bitcoinDict = {'time':time,'price':bitcoin_price,'fully_diluted_market_cap':fully_diluted_market_cap,
                            'market_cap':market_cap,'market_cap_dominance':market_cap_dominance,
                            'percent_change_1h':percent_change_1h,'percent_change_24h':percent_change_24h,
                            'percent_change_7d':percent_change_7d,'percent_change_30d':percent_change_30d,
                            'percent_change_60d':percent_change_60d,'percent_change_90d':percent_change_90d,
                            'volume_24h':volume_24h,'volume_change_24h':volume_change_24h,
                            'total_supply':total_supply,'max_supply':max_supply,'circulating_supply':circulating_supply
                            ,'num_buys':numBuys, 'num_sells':numSells}
            
            
            print(f"The current price of Bitcoin is: {bitcoin_price}")

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        
        bitcoinData = self.loadDataFile('bitcoinData.json')
        for key, value in bitcoinDict.items():
            if key in bitcoinData:
                bitcoinData[key].append(value)
            else:
                bitcoinData[key] = [value]
        
        self.saveData(bitcoinData, 'bitcoinData.json')

        return bitcoinDict
    
    def getTrainData(self):
        bitcoinData = self.loadDataFile('bitcoinData.json')
        x = np.column_stack(list(bitcoinData.values()))
        y = bitcoinData['y']
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        return x, x_train, x_test, y_train, y_test

    def runModel(self):
        model = svm.SVC(kernel='rbf',
                        gamma=0.1,
                        c=10.0)
        [x, x_train, x_test, y_train, y_test] = self.getTrainData()
        model.fit(x_train, y_train)
        dump(model, 'svm_model.joblib')
        accuracy = model.score(x_test, y_test)
        print(f"Model accuracy: {accuracy}")

    def predict(self):
        model_loaded = load('svm_model.joblib')
        bitcoinData = self.coinMarketApiCall()
        [X, _, _,  _, _] = self.getTrainData()
        predictions = model_loaded.predict(X)
        return predictions

    def saveData(self,dic, filename):
        with open(filename, 'w') as f:
            json.dump(dic, f)

    def loadDataFile(self,filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    def getGoogleData(self):

        # Initialize a TrendReq object
        pytrends = TrendReq(hl='en-US', tz=360)  # Adjust timezone if needed

        # Specify your search term
        keyword = ['bitcoin']  # Replace 'bitcoin' with your keyword of interest
        # keywords_list = ['bitcoin','blockchain','etherium','crypto']
        # Build the payload to fetch data
        pytrends.build_payload(kw_list=keyword, timeframe='now 1-d')

        # Fetch interest over time
        data = pytrends.interest_over_time()

        # Calculate the average interest for the past 24 hours
        # average_interest = data[keywords[0]].mean()

        # Print the average interest
        # print(f"Average interest for '{keywords[0]}' over the past 24 hours: {average_interest}")
        dataColumn = data[keyword]
        data_sum = dataColumn.sum()



        return data, data_sum
    
    def getTradingView(self):
        driver = webdriver.Chrome()
        driver.get("https://www.tradingview.com/symbols/BTCUSD/technicals/")
        # search = driver.find_element_by_id("1D")

        # search.send_keys
        tables = driver.find_elements(By.CLASS_NAME, "table-hvDpy38G")
        table1 = tables[0]
        table2 = tables[1]
        res = re.split(r'(\s)', table1.text)
        res = [x for x in res if x != '']
        res1 = re.split(r'(\s)', table2.text)
        res1 = [x for x in res1 if x != '']
        res = res + res1
        numSells = 0
        numBuys = 0
        for i in res:
            if i == 'Sell':
                numSells += 1
            elif i == 'Buy':
                numBuys += 1
        driver.quit()
        return numBuys, numSells

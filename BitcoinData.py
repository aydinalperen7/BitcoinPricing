# api key = b1ab10c3-8652-47d7-8e78-b1e855ae23c5
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pprint
import json
from datetime import datetime
import pytz
from sklearn import svm
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.model_selection import train_test_split
from joblib import dump, load

class GetBitcoinData():
    def __init__(self):
        self.bitcoinData = {}

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
        'X-CMC_PRO_API_KEY': 'b1ab10c3-8652-47d7-8e78-b1e855ae23c5',
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            pprint.pprint(data)
            bitcoin_price = data['data']['BTC']['quote']['USD']['price']
            time = data['data']['BTC']['quote']['USD']['last_updated']
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


            utc_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
            utc_time = pytz.utc.localize(utc_time)
            chicago_time = utc_time.astimezone(pytz.timezone("America/Chicago"))

            # time is calculated by the hour and minute normalized between 0 and 1
            # so if the time is 12:00pm, the hour will be 0.5 and the minute will be 0.0
            hour = chicago_time.hour/24
            minute = chicago_time.minute/1440
            time = hour + minute

            bitcoinDict = {'time':time,'price':bitcoin_price,'fully_diluted_market_cap':fully_diluted_market_cap,
                            'market_cap':market_cap,'market_cap_dominance':market_cap_dominance,
                            'percent_change_1h':percent_change_1h,'percent_change_24h':percent_change_24h,
                            'percent_change_7d':percent_change_7d,'percent_change_30d':percent_change_30d,
                            'percent_change_60d':percent_change_60d,'percent_change_90d':percent_change_90d,
                            'volume_24h':volume_24h,'volume_change_24h':volume_change_24h,
                            'total_supply':total_supply,'max_supply':max_supply,'circulating_supply':circulating_supply}
            
            
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
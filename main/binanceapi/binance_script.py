import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from binance.client import Client
import binance
from config import Binance

bina = Binance()

class Work:
    def __init__(self, apik, secretk):
        self.key_api = apik
        self.key_secret = secretk

    def response_check(self):
        client = Client(self.key_api, self.key_secret)
        code = 200
        try:
            getacc = client.get_account()
        except binance.exceptions.BinanceAPIException as e:
            code = e.status_code
        if code!=200:
            self.key_api = bina.API_KEY
            self.key_secret = bina.SECRET_KEY
            return 0
        return 1

    def crypto_details(self, symb):
        client = Client(self.key_api, self.key_secret)
        opts = bina.SYMBOLS
        ticker_data = client.get_ticker()[opts.index(symb)]
        return ticker_data

    def account_balance(self):
        client = Client(self.key_api, self.key_secret)
        balance = client.get_account()
        return balance

    def hist_data(self, symbol, interval, time):
        client = Client(self.key_api, self.key_secret)
        histodata = client.get_historical_klines(symbol, eval(f"Client.KLINE_INTERVAL_{interval}"), time)
        return histodata

# w = Work(bina.API_KEY, bina.SECRET_KEY)
# print(w.hist_data("ETHBTC", "12HOUR", "1 month ago"))
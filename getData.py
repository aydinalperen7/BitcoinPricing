from BitcoinData import *
from dotenv import load_dotenv
import os
load_dotenv()
apiKey = os.getenv("API_KEY")
print(apiKey)
GetBitcoinData(apiKey).coinMarketApiCall()

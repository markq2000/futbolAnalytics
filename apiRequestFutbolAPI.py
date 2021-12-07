import os
import requests
from dotenv import load_dotenv
load_dotenv()

TRANSFER_API_KEY = os.getenv("TRANSFER_API_KEY")

# Testing API request to get seasonal data for FC Barcelona
url = "https://transfermarket.p.rapidapi.com/transfers/list-by-club"
querystring = {"id":"131","seasonID":"2000"}
headers = {
    'x-rapidapi-host': "transfermarket.p.rapidapi.com",
    'x-rapidapi-key': TRANSFER_API_KEY
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())


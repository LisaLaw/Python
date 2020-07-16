import requests
from fatsecret import Fatsecret
import json

token_url = 'https://oauth.fatsecret.com/connect/token'

params = {
    'grant_type': 'client_credentials',
    'client_id': '3e7e91f7555c405ea68bba257c6b9bba',
    'client_secret': 'da4e34bb887d490483a05f2c86fbe3b8',
    'scope': 'basic',
}

token = requests.post(token_url, params)
print(token)
data = token.json()
print(data)
print("")
print('My token is ', data['access_token'])
print("")


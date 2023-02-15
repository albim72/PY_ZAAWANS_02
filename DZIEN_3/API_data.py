import requests
import json

response = requests.get('https://example.com/api/data')

response_text = response.text
response_json = response.json()

response = requests.get('https://example.com/api/data', params={'param1': 'value1', 'param2': 'value2'})

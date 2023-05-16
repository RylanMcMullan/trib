from pip._vendor import requests
import json

response = requests.get('https://randomuser.me/api/')
"""print(type(response))
print(response)
print(type(response.text))
print(response.text)"""

response_json = json.loads(response.text)
#print(type(response_json))

person = response_json['results'][0]

for key in person:
    print(f"{key}: {person[key]}")
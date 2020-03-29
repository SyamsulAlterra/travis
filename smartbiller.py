import requests

url = "https://smartbiller-staging.sumpahpalapa.com/"
response = requests.get(url)
# print(dir(response))
print(response.text)
import requests

url = "https://cmdb.pieter.fish/api/cmdb/devices"
headers = {}
params = {}
response = requests.get(url)
data = response.json()

print(data)

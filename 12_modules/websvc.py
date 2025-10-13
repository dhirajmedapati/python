# Working with some API 
import requests

url = "https://python.org/"
res = requests.get(url)
print(res.status_code)
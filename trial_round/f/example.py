import requests
import json

def main():
  url = input().strip()
  port = input().strip()
  a = input().strip()
  b = input().strip()

  url = url + ':' + port

  params = { 
    'a': a,
    'b': b
  }

  response = requests.get(url, params=params)
  json_data = response.json()
  print(sum(json_data))
  
main()
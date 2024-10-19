import requests
request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request)
json = response.json()
joke = json["value"]
print(joke)


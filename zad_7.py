import requests

class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str, city: str, state: str, website_url: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.website_url = website_url

    def __str__(self):
        return f"Name: {self.name}, City: {self.city}, Type: {self.brewery_type}, Site: {self.website_url}"

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
response = requests.get(url)
data = response.json()

brewery_list = []

for item in data:
    b = Brewery(
        item.get('id'),
        item.get('name'),
        item.get('brewery_type'),
        item.get('city'),
        item.get('state_province'),
        item.get('website_url')
    )
    brewery_list.append(b)

for brewery in brewery_list:
    print(brewery)
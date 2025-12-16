import requests
import argparse


class Brewery:
    def __init__(
            self,
            id: str,
            name: str,
            brewery_type: str,
            city: str, state: str,
            website_url: str
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.state = state
        self.website_url = website_url

    def __str__(self):
        return (f"Name: {self.name}, City: {self.city}, "
                f"Type: {self.brewery_type}, Site: {self.website_url}")


parser = argparse.ArgumentParser()
parser.add_argument('--city', type=str)
args = parser.parse_args()

url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

if args.city:
    city_param = args.city.replace(" ", "_")
    url = f"https://api.openbrewerydb.org/v1/breweries?by_city={city_param}&per_page=20"  # noqa: E501

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

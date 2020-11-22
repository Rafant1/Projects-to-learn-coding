# This project will use an external and free star wars API to allow the user search for a certain information from the star wars universe
# API documentation url address: https://swapi.dev/documentation
import requests

r = requests.get('https://swapi.dev/api')
r_dict = r.json()
print(r_dict)

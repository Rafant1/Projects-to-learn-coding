# This project will use an external and free star wars API to allow the user search for a certain information from the star wars universe
# API documentation url address: https://swapi.dev/documentation
import requests


def planet_info():
    r2 = requests.get('https://swapi.dev/api/planets/')
    r2_dict = r2.json()
    print('About which planet you would like to get more information?')

    for planet in r2_dict['results']:
        print(planet['name'])
    player_choice = input('Planet\'s name: ')

    for planet in r2_dict['results']:
        if planet['name'] == player_choice:
            print("\nplanet's name:", planet['name'])
            print("rotation period [in hours]:", planet['rotation_period'])
            print("orbital period [in days]:", planet['orbital_period'])
            print("diameter [in kilometers]:", planet['diameter'])
            print("climate:", planet['climate'])
            print("primary terrain[s]:", planet['terrain'])
            print("population size:", planet['population'])

            name_list = []

            for element in planet['residents']:
                person = requests.get(element)
                person_dict = person.json()
                name_list.append(person_dict['name'])

            if name_list:
                print("the most fameous people born on this planet: ", end="")
                print(*name_list, sep=', ')
            else:
                print("There are not any known fameous people born on this planet.")




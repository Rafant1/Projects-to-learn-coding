# This project will use an external and free star wars API to allow the user search for a certain information from the star wars universe
# API documentation url address: https://swapi.dev/documentation
import requests


def get_person():
    r1 = requests.get('https://swapi.dev/api/people/')
    r1_dict = r1.json()
    print('About which person would you like to get more information?')
    for person in r1_dict['results']:
        print(person['name'])

    player_choice = input('Person\'s name: ')
    for person in r1_dict['results']:
        if person['name'] == player_choice:
            print('name:',person['name'])
            print('gender:',person['gender'])
            print('birth year:', person['birth_year'])
            print('height [in centimeters]:',person['height'])
            print('mass: [in kilograms]',person['mass'])
            print('hair color:',person['hair_color'])
            print('skin color:',person['skin_color'])
            print('eye color:',person['eye_color'])

            home_world = requests.get(person['homeworld'])
            home_world_dict = home_world.json()
            print('homeworld:',home_world_dict['name'])

            films_list = []
            for element in person['films']:
                element = requests.get(element)
                films_dict = element.json()
                films_list.append(films_dict['title'])
            print('Appearance(s) in films: ', end= '')
            print(*films_list, sep= ', ')


def get_planet():
    r2 = requests.get('https://swapi.dev/api/planets/')
    r2_dict = r2.json()
    print('About which planet would you like to get more information?')

    for planet in r2_dict['results']:
        print(planet['name'])

    player_choice = input('Planet\'s name: ')
    for planet in r2_dict['results']:
        if planet['name'] == player_choice:
            print('\nplanet\'s name:', planet['name'])
            print('rotation period [in hours]:', planet['rotation_period'])
            print('orbital period [in days]:', planet['orbital_period'])
            print('diameter [in kilometers]:', planet['diameter'])
            print('climate:', planet['climate'])
            print('primary terrain[s]:', planet['terrain'])
            print('population size:', planet['population'])

            name_list = []

            for element in planet['residents']:
                element = requests.get(element)
                person_dict = element.json()
                name_list.append(person_dict['name'])

            if name_list:
                print("the most fameous people born on this planet: ", end="")
                print(*name_list, sep=', ')
            else:
                print("There are not any known fameous people born on this planet.")


get_person()


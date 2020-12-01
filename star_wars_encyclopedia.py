# This project will use an external and free star wars API to allow the user search for a certain information from the star wars universe
# API documentation url address: https://swapi.dev/documentation
import requests

def check_name():

    url_adresses = ['http://swapi.dev/api/people/',
                    'http://swapi.dev/api/planets/',
                    'http://swapi.dev/api/films/',
                    'http://swapi.dev/api/species/',
                    'http://swapi.dev/api/vehicles/',
                    'http://swapi.dev/api/starships/']

    # Why are there 3 check_presence variables?
    # Because we want to find the user's input inside the API's base even if it is introduced with small letter
    # (which do variable check_presence and check_presence_2
    # in our API there are also names like X-wing. In this case, title method doesn't work because it thinks that
    # x and wing are two separate words. In order to fix this situation (for example, if user writes x-wing), we use
    # capitalize method
    check_presence = input('write a name to check if it is present in our database: ')
    check_presence_2 = check_presence.title()
    check_presence_3 = check_presence.capitalize()

    list = []
    correct_guess = []

    # First, we create a for loop to establish connection with every API url address.
    # Then we iterate through elements in each address to get access to key 'results' in dictionary
    # and we save that information as a list (but the elements inside the list stay as dictipnary).
    # Then we use for loop, to get each key name and other for loop to check if user's input name
    # is the same as any existing value of keys in key 'results' dictionary.
    # how the information is packed:
    # {'previous': None, 'results': [{'name': 'Tatooine', 'rotation_period': 23'}]

    for element in url_adresses:
        element = requests.get(element)
        category_dict = element.json()
        for element in category_dict['results']:
            list.append(element)

    for element in list:
        try:
            guess = element
        except KeyError:
            print('blad')

        for key in guess:
            if check_presence == guess[key] or check_presence_2 == guess[key] or check_presence_3 == guess[key]:
                print('this name appears in our database')
                correct_guess.append(check_presence)

    if not correct_guess:
        print('unfortunately, there is no such name in our dictionary')


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
            print('mass [in kilograms]:',person['mass'])
            print('hair color:',person['hair_color'])
            print('skin color:',person['skin_color'])
            print('eye color:',person['eye_color'])

            #home_world key value is url, that's why we had to send another request
            #in home_world there is only one url, so we don't have to use for loop
            home_world = requests.get(person['homeworld'])
            home_world_dict = home_world.json()
            print('homeworld:',home_world_dict['name'])

            films_list = []

            # We use for loop here because some keys' values are urls, so we have to send another request
            # The same situation will appear in other get functions
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


def get_film():
    r3 = requests.get('https://swapi.dev/api/films/')
    r3_dict = r3.json()
    print('About which film would you like to get more information?')

    for film in r3_dict['results']:
        print(film['title'])

    player_choice = input('film\'s title: ')
    for film in r3_dict['results']:
        if film['title'] == player_choice:
            print('\ntitle:',film['title'])
            print('\ndirector:', film['director'])
            print('producer[s]:', film['producer'])
            print('release date:', film['release_date'])
            print('which film in the Star Wars saga:',film['episode_id'])
            print('\nopening crawl:')
            print(film['opening_crawl'])

            characters_list = []
            for element in film['characters']:
                element = requests.get(element)
                characters_dict = element.json()
                characters_list.append(characters_dict['name'])
            print('\ncharacters that are seen in this film: ', end= '')
            print(*characters_list, sep=', ')

            planets_list = []
            for element in film['planets']:
                element = requests.get(element)
                planets_dict = element.json()
                planets_list.append(planets_dict['name'])
            print('planets that appear in this film: ', end='')
            print(*planets_list, sep=', ')

            starships_list = []
            for element in film['starships']:
                element = requests.get(element)
                starships_dict = element.json()
                starships_list.append(starships_dict['name'])
            print('starships presented in this film: ', end='')
            print(*starships_list, sep=', ')

            vehicles_list = []
            for element in film['vehicles']:
                element = requests.get(element)
                vehicles_dict = element.json()
                vehicles_list.append(vehicles_dict['name'])
            print('vehicles that appear in this film: ', end='')
            print(*vehicles_list, sep=', ')

            species_list = []
            for element in film['species']:
                element = requests.get(element)
                species_dict = element.json()
                species_list.append(species_dict['name'])
            print('species that are seen in this film: ', end='')
            print(*species_list, sep=', ')



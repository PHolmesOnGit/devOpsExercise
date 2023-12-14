"""

API Call To-Do:

- Make a function that gets the needed data from input.yaml to make a successful call to the Star Wars API - DONE

- Make a function that calls the swapi and turns the response into a list to be digested in the FileExport Class - DONE


"""

import yaml
import requests


class CallStarWarsAPI:

    def get_data_from_file(self):
        # Gets ID and type data from input.yaml, which will be used for the api call
        with open('input.yaml') as f:
            dict = yaml.load(f, Loader=yaml.FullLoader)
            data = dict['input']
            id_list = []
            type_list = []
            counter = 0
            for stuff in data:
                id_list.append(data[counter]['id'])
                type_list.append(data[counter]['type'])
                counter += 1

        return id_list, type_list

    def make_api_call(self, type_list, id_list):
        # makes the api call using the ID and type data, returns the api response
        url = "https://swapi.dev/api/"
        counter = 0
        data_list = []

        while counter < len(id_list):
            response = requests.request('GET', url=f"{url}{type_list[counter]}/{id_list[counter]}/")
            print(response.raise_for_status())
            print(f"calling swapi for type={type_list[counter]} and for id={id_list[counter]}")
            data = response.json()
            print(data)
            data_list.append(data)
            counter += 1

        return data_list


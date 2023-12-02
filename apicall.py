import yaml
import requests


class CallStarWarsAPI:
    def __init__(self):
        self.get_data_from_file()

    def get_data_from_file(self):
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


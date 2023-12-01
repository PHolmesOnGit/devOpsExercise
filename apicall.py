import yaml


class CallStarWarsAPI:
    def __init__(self):
        self.get_data_from_file()
        self.make_api_call()

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

    def make_api_call(self):
        pass

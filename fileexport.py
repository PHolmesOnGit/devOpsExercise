"""

File Export to-do

- Read info request data in input.yaml and get that data from the response of the swapi. - DONE

- Construct a json file organized with the requested data - DONE

- Add that file to a directory that lives outside the project. - DONE

"""
import json
import yaml
import os


class FileExport:

    def get_data_and_turn_into_json_file(self, api_response):
        # Gets the 'infoRequest' data from input.yaml and gets the swapi response of the relevant data
        # Converts that data into a dict to use as our json file
        counter = 0
        while counter < len(api_response):
            info_dict = {}
            with open('input.yaml') as f:
                dict = yaml.load(f, Loader=yaml.FullLoader)
                data = dict['input'][counter]['infoRequest']
                for i in data:
                    info_dict[i] = api_response[counter][i]
                print(f"Dict for {info_dict['name']}")
                print(info_dict)

                def export_json_file_to_external_directory(info_dict):
                    # This function takes info_dict and turns it into a json object
                    # Once converted,  we write the json object as a file into the users Documents folder
                    json_object = json.dumps(info_dict, indent=4)

                    file_name = f"{info_dict['name']}.json"

                    with open(os.path.join(os.path.expanduser('~'), 'Documents', file_name), "w") as outfile:
                        outfile.write(json_object)

                export_json_file_to_external_directory(info_dict)
            counter += 1

"""
Test to-do

- Verify that there is an input.yaml file

- test function call to star wars API with a test input

- test function that outputs data into json files in a directory

"""

import yaml
import requests



def verify_input_file_exists():
    try:
        with open('input.yaml') as f:
            dict = yaml.load(f, Loader=yaml.FullLoader)
            print(dict)
            print("Test verify input file exists succeeded")
    except FileNotFoundError:
        print("Test verify input file exists failed: No input.yaml file")


def test_swapi_call():
    test_url = "https://swapi.dev/api/planets/1"
    response = requests.request('GET', test_url)
    try:
        print(response.raise_for_status())
        print(response.json())
    except requests.exceptions.HTTPError:
        print("Test no work it fail")




verify_input_file_exists()
test_swapi_call()
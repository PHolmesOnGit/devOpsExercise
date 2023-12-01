"""

Main to-do

- import input.yaml data

- create a function that ingests the input.yaml data into proper headers to make a call to the star wars API

- create a function that jsonifies the data from the star wars api (if it isn't already) and exports a json
file with the data to a directory that exists outside the project.

"""

import yaml

from apicall import CallStarWarsAPI

call_api = CallStarWarsAPI()

print(call_api.get_data_from_file())



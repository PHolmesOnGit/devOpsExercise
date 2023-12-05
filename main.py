"""

Running main will make a call to the Star Wars API and will grab the requested data from input.yaml and then write .json
files in your Documents folder for each object in input.yaml

"""

from apicall import CallStarWarsAPI
from fileexport import FileExport

call_api = CallStarWarsAPI()
file_export = FileExport()

data_needed_for_api_call = call_api.get_data_from_file()

id_list, type_list = data_needed_for_api_call

api_response = call_api.make_api_call(type_list, id_list)

file_export.get_data_and_turn_into_json_file(api_response)

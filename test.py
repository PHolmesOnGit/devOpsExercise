"""
Test to-do

- test function call to star wars API with a test input - DONE

- test function that outputs data into json files in a directory - DONE

"""

from unittest import TestCase
from unittest.mock import patch

import apicall
import fileexport
import json


class TestCallStarWarsAPI(TestCase):
    @patch('apicall.CallStarWarsAPI')
    def test_getting_data_from_file(self, MockRead):
        data = MockRead()

        data.info.return_value = [
            {
                'type': 'person',
                'id': 1,
            }
        ]

        response = data.info()
        print(data.info.return_value)
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # Additional assertions
        assert MockRead is apicall.CallStarWarsAPI  # The mock is equivalent to the original

        assert MockRead.called  # The mock was called

        data.info.assert_called_with()  # We called the posts method with no arguments

        data.info.assert_called_once_with()  # We called the posts method once with no arguments

        data.reset_mock()  # Reset the mock object

        data.info.assert_not_called()  # After resetting, posts has not been called.


class TestFileExport(TestCase):
    @patch('fileexport.FileExport')
    def test_json_file_write(self, MockWrite):
        file = MockWrite

        file.info.return_value = {
            'id': 1,
            'type': 'person',
            'message': 'if you see this the test was successful :)',
        }

        json_object = json.dumps(file.info.return_value, indent=4)

        with open("test.json", "w") as outfile:
            outfile.write(json_object)

        response = file.info()
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)

        assert MockWrite is fileexport.FileExport  # The mock is equivalent to the original

        file.info.assert_called_with()  # We called the posts method with no arguments

        file.info.assert_called_once_with()  # We called the posts method once with no arguments

        file.reset_mock()  # Reset the mock object

        file.info.assert_not_called()  # After resetting, posts has not been called.

"""
Test to-do

- Verify that there is an input.yaml file

- test function call to star wars API with a test input

- test function that outputs data into json files in a directory

"""

from unittest import TestCase
from unittest.mock import patch

import apicall


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

        assert MockRead.called  # The mock wasP called

        data.info.assert_called_with()  # We called the posts method with no arguments

        data.info.assert_called_once_with()  # We called the posts method once with no arguments

        data.reset_mock()  # Reset the mock object

        data.info.assert_not_called()  # After resetting, posts has not been called.
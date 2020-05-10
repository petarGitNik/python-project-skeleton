import unittest
from unittest import mock
from project.project import ApiWrapper


class MockHTTPResponse:

    def __init__(self, return_value):
        self.return_value = return_value

    def json(self):
        return self.return_value



class ApiWrapperTestCase(unittest.TestCase):

    def setUp(self):
        self.wrapper = ApiWrapper('https://api.example.com')

    @mock.patch(
        'requests.get',
        mock.MagicMock(
            return_value=MockHTTPResponse([{'1': 'user1'}, {'2': 'user2'}])
        )

    )
    def test_get_endpoint(self):
        response = self.wrapper.get('users/')
        self.assertEqual(response, [{'1': 'user1'}, {'2': 'user2'}])

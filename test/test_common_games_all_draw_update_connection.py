from unittest import TestCase
import unittest
import requests
from main import start_flask_api_server


class TestCommonGames(TestCase):

    def setUp(self):
        host = "localhost"
        port = 6001
        debug = True

        self.api = start_flask_api_server(host, port, debug)

        self.request_url = f"http://{host}:{port}/" + "{}/{}"
        pass

    def test_common_game_request_all_draw_update_connection(self):
        response = requests.get(self.request_url.format("all", "draw_update"))
        self.assertTrue(response.ok)

    def tearDown(self):
        self.api.shutdown()


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase
import unittest
import requests
from main import start_flask_api_server


class TestCommonGames(TestCase):

    def setUp(self):
        host = "localhost"
        port = 6004
        debug = True

        self.api = start_flask_api_server(host, port, debug)

        self.request_url = f"http://{host}:{port}/" + "{}/{}"

        self.games = [
            'lotto',
            'lotto_plus1',
            'lotto_plus2',
            'powerball',
            'powerball_plus',
        ]
        pass

    def test_common_game_request_history_connection(self):
        for game in self.games:
            response = requests.get(self.request_url.format(game, "history"))
            self.assertTrue(response.ok)

    def tearDown(self):
        self.api.shutdown()


if __name__ == '__main__':
    unittest.main()

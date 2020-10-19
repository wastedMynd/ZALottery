from unittest import TestCase
import unittest
import requests
from main import start_flask_api_server
from __init__ import Logging

logger = Logging().get_logger()


class TestCommonGames(TestCase):

    def setUp(self):
        host = "localhost"
        port = 6006
        debug = True

        logger.debug(f"Server... started at {host}:{port} with debug being {debug}.")
        self.api = start_flask_api_server(host, port, debug)
        logger.debug(f"Server is running.. {self.api}")

        self.request_url = f"http://{host}:{port}/" + "{}/{}"

        self.games = [
            'lotto',
            'lotto_plus1',
            'lotto_plus2',
            'powerball',
            'powerball_plus',
        ]
        pass

    def test_common_game_request_quick_pick_connection(self):
        for game in self.games:
            with requests.get(self.request_url.format(game, "quick_pick")) as response:
                self.assertTrue(response.ok)
                logger.debug(f"response is {response.json()}")

    def tearDown(self):
        logger.debug("Server is now about to shutdown...")
        self.api.shutdown()
        logger.debug(f"Server is now.. {self.api}")


if __name__ == '__main__':
    logger.debug("Starting test...")
    unittest.main()
    logger.debug("Ending test!")

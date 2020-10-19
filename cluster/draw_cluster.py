import requests
from cluster.__init__ import get_cluster_url, get_cluster_properties
from resource.__init__ import get_game_draw_url, get_game_draw_history_url
from pymongo import MongoClient

games = ["lotto", "lotto_plus1", "lotto_plus2", "powerball", "powerball_plus"]


def update_game_draw_result(game: str) -> dict:
    return DrawCluster(game).update_draw_result()


def update_all_games_draw_result() -> dict:
    return {"payload": [update_game_draw_result(game) for game in games]}


def update_game_draw_result_history(game: str) -> dict:
    return DrawCluster(game).update_draw_history_result()


def update_all_game_draw_history() -> dict:
    return {"payload": [update_game_draw_result_history(game) for game in games]}


class DrawCluster:

    def __init__(self, game: str):

        self.cluster = MongoClient(get_cluster_url())

        self.properties = get_cluster_properties()

        self.game = game

    def update_draw_result(self) -> dict:

        database = self.cluster[self.properties.get("cluster")["database_draw"]]

        collection = database[self.game]

        with requests.get(get_game_draw_url(self.game)) as response:
            response_json = response.json()

        key = "draw_id"

        online_draw_id = response_json[key]

        has_document = True

        cluster_draw = None
        try:
            cluster_draw = collection.find_one({key: online_draw_id})
            has_document = False if cluster_draw is None else cluster_draw[key] == online_draw_id
        finally:

            print(f"{cluster_draw=}")

            if cluster_draw is None or not has_document:
                collection.insert_one(response_json)

            if has_document:
                return {
                    'game': self.game,
                    'updated': False,
                    'payload': response_json
                }
            else:
                return {
                    'game': self.game,
                    'updated': True,
                    'payload': response_json
                }

    def update_draw_history_result(self) -> dict:

        database = self.cluster[self.properties.get("cluster")["database_draw_history"]]

        collection = database[self.game]

        with requests.get(get_game_draw_history_url(self.game)) as response:
            response_json = response.json()

        draw_history = response_json

        draw_history_list = draw_history["draw_history_result_list"]

        draw_id_key = "draw_id"
        updated = False
        for draw_update in draw_history_list:
            has_document = False
            this_draw_id = draw_update[draw_id_key]
            this_draw_id_content = {draw_id_key: this_draw_id}
            try:
                cluster_draw = collection.find_one(this_draw_id_content)
                cluster_draw_id = cluster_draw[draw_id_key]

                is_draw_present = cluster_draw_id == this_draw_id
                has_document = False if cluster_draw is None else is_draw_present
            finally:
                updated = has_document
                if not has_document:
                    collection.insert_one(draw_update)

        return {
            'game': self.game,
            'updated': updated,
            'payload': draw_history
        }


if __name__ == '__main__':
    print(update_all_games_draw_result())

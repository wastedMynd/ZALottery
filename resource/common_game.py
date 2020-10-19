from flask_restful import Resource
from scrapper.common_games.draw_scrapper import get_draw as get_draw_online
from resource.quickpick import get_quick_pick
from scrapper.common_games.history_scrapper import get_history
from cluster.draw_cluster import update_game_draw_result,\
    update_all_games_draw_result, update_game_draw_result_history, update_all_game_draw_history
from resource.game_info import GameInfo


class CommonGameResources(Resource):
    def get(self, game_name, function="info") -> dict:

        game_info = GameInfo.LOTTO

        if game_name == "all" and function == "draw_update":
            return update_all_games_draw_result()
        elif game_name == "all" and function == "history_update":
            return update_all_game_draw_history()
        else:
            for this_game in GameInfo:
                try:
                    if this_game.value[0]['game_name'] == game_name:
                        game_info = this_game
                        break
                except KeyError:
                    if this_game.value['game_name'] == game_name:
                        game_info = this_game
                        break

            if function == "info":
                try:
                    return game_info.value[0]
                except KeyError:
                    return game_info.value
            elif function == "draw":
                try:
                    return get_draw_online(game_info.value[0]["latest_draw_result_url"])
                except KeyError:
                    return get_draw_online(game_info.value["latest_draw_result_url"])
            elif function == "draw_update":
                return update_game_draw_result(game_name)
            elif function == "history":
                try:
                    return get_history(game_info.value[0]["draw_history_url"])
                except KeyError:
                    return get_history(game_info.value["draw_history_url"])
            elif function == "history_update":
                return update_game_draw_result_history(game_name)
            elif function == "quick_pick":
                return get_quick_pick(game_name)
            else:
                try:
                    return {function: dict(game_info.value[0])[function]}
                except KeyError:
                    return {function: dict(game_info.value)[function]}

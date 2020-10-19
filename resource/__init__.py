from resource.game_info import GameInfo


def get_game_draw_url(game) -> str:
    return f"http://localhost:5000/{game}/draw"

def get_game_draw_history_url(game) -> str:
    return f"http://localhost:5000/{game}/history"

def get_draw_info_draw_datetime(game_type) -> dict:
    draw_date = None
    draw_time = None
    is_game_type_found = False

    gameInfo = None
    for game in GameInfo:
        if game_type.lower() == game.name.lower():
            gameInfo = game.value[0]
            is_game_type_found = True
            break

    if is_game_type_found:
        draw_date = gameInfo["draw_date"]
        draw_time = gameInfo["draw_time"]

    return {
        "game_type": game_type,
        "draw_date": draw_date,
        "draw_time": draw_time,
        "is_game_type_found": is_game_type_found
    }

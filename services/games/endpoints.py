from config.env import HOST


class Endpoints:
    get_games_list = f'{HOST}/games'
    get_games_search = f'{HOST}/games/search'
    get_games_for_uuid = lambda self, game_uuid: f'{HOST}/games/{game_uuid}'

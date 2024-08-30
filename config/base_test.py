from services.users.users_api import UsersAPI
from services.games.games_api import GamesAPI


class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()
        self.api_games = GamesAPI()

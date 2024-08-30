import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Администрирование над играми")
@allure.feature("Игра")
class TestGames(BaseTest):

    @pytest.mark.regression
    @allure.story("Получение списка игр")
    @allure.title('Успешное получение игр по лимиту')
    def test_get_all_games(self):
        self.api_games.get_all_games(offset=0, limit=10)

    @pytest.mark.regression
    @allure.story("Получение игры по названию")
    @allure.title('Успешное получение игры по названию')
    def test_get_game_by_query(self):
        self.api_games.get_game_by_query(offset=0, limit=10, query="Baldur's Gate 3")

    @pytest.mark.regression
    @allure.story("Получение игры по uuid")
    @allure.title('Успешное получение игры по названию uuid')
    def test_get_game_by_uuid(self):
        uuid = self.api_games.get_uuid_game_by_title(offset=0, limit=10, query="Baldur's Gate 3")
        self.api_games.get_game_by_uuid(uuid)

import allure
import requests
from utils.helper import Helper, helper
from services.games.endpoints import Endpoints
from config.headers import Headers
from services.games.models.games_model import MainModel, GameModel


class GamesAPI(Helper):
    def __init__(self):
        super().__init__()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Получение всех игр")
    def get_all_games(self, offset=0, limit=10):
        with allure.step(f'Отправление запроса с параметрами offset: {offset}, limit: {limit}'):
            response = requests.get(
                params={
                    'offset': offset,
                    'limit': limit
                },
                url=self.endpoints.get_games_list,
                headers=self.headers.basic
            )
            helper.api_request(response)
            assert response.status_code == 200, response.json()
            self.attach_response(response.json())
            MainModel(**response.json())
            json_data = response.json()
            value = json_data.get("games")
            return value

    @allure.step("Получение игры по названию")
    def get_game_by_query(self, offset=0, limit=10, query=''):
        with allure.step(f'Отправление запроса с параметрами offset: {offset}, limit: {limit}, query: {query}'):
            params = {
                'offset': offset,
                'limit': limit
            }

            # Добавляем параметр query только если он не пустой
            if query:
                params['query'] = query

            response = requests.get(
                url=self.endpoints.get_games_search,
                headers=self.headers.basic,
                params=params
            )
            helper.api_request(response)
            assert response.status_code == 200, response.json()
            assert response.json()['games'][0]['title'] == query
            self.attach_response(response.json())
            MainModel(**response.json())
            json_data = response.json()
            value = json_data.get("games")
            return value

    @allure.step("Получение uuid игры по title")
    def get_uuid_game_by_title(self, offset=0, limit=10, query=''):
        with allure.step(f'Получение игры по параметру query: {query}'):
            params = {
                'offset': offset,
                'limit': limit
            }

            # Добавляем параметр query только если он не пустой
            if query:
                params['query'] = query

            response = requests.get(
                url=self.endpoints.get_games_search,
                headers=self.headers.basic,
                params=params
            )
            helper.api_request(response)
            self.attach_response(response.json())
            MainModel(**response.json())
            assert response.json()['games'][0]['title'] == query
            uuid = response.json()['games'][0]['uuid']
            return uuid

    @allure.step("Получение игры по uuid")
    def get_game_by_uuid(self, uuid):
        with allure.step(f'Получение игры по параметру uuid: {uuid}'):
            params = {}
            if uuid:
                params['uuid'] = uuid
            response = requests.get(
                url=self.endpoints.get_games_for_uuid(uuid),
                headers=self.headers.basic,
                params=params
            )
            helper.api_request(response)
            self.attach_response(response.json())
            GameModel(**response.json())
            assert response.status_code == 200, response.json()
            assert response.json()['uuid'] == uuid

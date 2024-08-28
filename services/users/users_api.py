import allure
import requests

from utils.helper import Helper
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from config.headers import Headers
from services.users.models.user_model import UserModel, UserModelDelete, UserResponse


class UsersAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Создание пользователя")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user

        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Получение всех пользователей")
    def get_all_users(self, offset=0, limit=10):
        response = requests.get(
            params={
                'offset': offset,
                'limit': limit
            },
            url=self.endpoints.get_user_list,
            headers=self.headers.basic
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        UserResponse(**response.json())
        json_data = response.json()
        value = json_data.get("users")
        return value

    @allure.step("Получение пользователя по uuid")
    def get_user_by_id(self, uuid):
        try:
            response = requests.get(
                url=self.endpoints.get_user_by_id(uuid),
                headers=self.headers.basic,

            )
            assert response.status_code == 200, response.json()
            self.attach_response(response.json())
            model = UserModel(**response.json())
            return model
        except AssertionError:
            print(f'Пользователь с данным uuid: {uuid} не найден')

    @allure.step("Получение пользователя по user_name")
    def get_uuid_by_name(self, data, name):
        for user in data:
            if user['name'] == name:
                return user['uuid']
        return None

    @allure.step("Удаление пользователя")
    def delete_user(self, uuid):
        response = requests.delete(
            url=self.endpoints.delete_user(uuid),
            headers=self.headers.basic,

        )
        assert response.status_code == 204, response.json()

    @allure.step("Изменение пользователя")
    def update_user(self, uuid):
        response = requests.patch(
            url=self.endpoints.update_user(uuid),
            headers=self.headers.basic,

        )
        assert response.status_code == 200, response.json()

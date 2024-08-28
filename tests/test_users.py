import allure
import pytest

from config.base_test import BaseTest


@allure.epic("Administration")
@allure.feature("Пользователи")
class TestUsers(BaseTest):

    @pytest.mark.regression
    @allure.title('Получение пользователей по лимиту')
    def test_get_all_user(self):
        self.api_users.get_all_users(offset=0, limit=10)

    @pytest.mark.regression
    @allure.title('Создание пользователя')
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user.uuid)

    @pytest.mark.regression
    @allure.title('Удаление пользователя')
    def test_delete_user(self):
        data = self.api_users.get_all_users()
        user_uuid = self.api_users.get_uuid_by_name(data, name="Alex")
        self.api_users.delete_user(user_uuid)
        self.api_users.get_user_by_id(user_uuid)

    @pytest.mark.regression
    @allure.title('Изменение пользователя')
    def test_update_user(self):
        data = self.api_users.get_all_users()
        user_uuid = self.api_users.get_uuid_by_name(data, name="Alex")
        self.api_users.update_user(user_uuid)

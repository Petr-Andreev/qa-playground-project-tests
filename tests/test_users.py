import allure
import pytest
from config.base_test import BaseTest


@allure.epic("Администрирование над пользователями")
@allure.feature("Пользователь")
class TestUsers(BaseTest):

    @pytest.mark.regression
    @allure.story("Получение списка пользователей")
    @allure.title('Успешное получение пользователей по лимиту')
    def test_get_all_user(self):
        self.api_users.get_all_users(offset=0, limit=10)

    @pytest.mark.regression
    @allure.story("Создание нового пользователя")
    @allure.title('Успешное создание нового пользователя')
    def test_create_user(self):
        user = self.api_users.create_user()
        self.api_users.get_user_by_id(user.uuid)

    @pytest.mark.regression
    @allure.story("Удаление пользователя")
    @allure.title('Успешное удаление пользователя')
    def test_delete_user(self):
        data = self.api_users.get_all_users()
        user_uuid = self.api_users.get_uuid_by_name(data, name="Alex")
        self.api_users.delete_user(user_uuid)
        self.api_users.get_user_by_id(user_uuid)

    @pytest.mark.regression
    @allure.story("Изменение пользователя")
    @allure.title('Успешное изменение пользователя по заданным параметрам')
    def test_update_user(self):
        data = self.api_users.get_all_users()
        user_uuid = self.api_users.get_uuid_by_name(data, name="John")
        self.api_users.update_user(user_uuid)
        self.api_users.get_user_by_id(user_uuid)

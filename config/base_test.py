from services.users.users_api import UsersAPI


class BaseTest:

    def setup_method(self):
        self.api_users = UsersAPI()

from config.env import HOST


class Endpoints:
    create_user = f'{HOST}/users'
    delete_user = lambda self, uuid: f'{HOST}/users/{uuid}'
    get_user_list = f'{HOST}/users'
    get_user_by_id = lambda self, uuid: f'{HOST}/users/{uuid}'
    update_user = lambda self, uuid: f'{HOST}/users/{uuid}'

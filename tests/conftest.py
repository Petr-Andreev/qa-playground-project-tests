import os
import pytest
import requests
from config.env import HOST


@pytest.fixture(autouse=True, scope='session')
def init_session():
    response = requests.post(
        url=f'{HOST}/setup',
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 205

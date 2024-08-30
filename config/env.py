import os

from dotenv import load_dotenv

load_dotenv()
STAGE = os.getenv('STAGE', default='prod')
HOST = 'https://dev-gs.qa-playground.com/api/v1' if STAGE == 'qa' else 'https://release-gs.qa-playground.com/api/v1'

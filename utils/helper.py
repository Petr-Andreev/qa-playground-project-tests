import allure
import json
from allure_commons.types import AttachmentType

from utils.attach import response_logging, response_attaching


class Helper:
    """
    Прикрепляет json из response к allure отчету
    """

    def attach_response(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name='API response', attachment_type=AttachmentType.JSON)

    def api_request(self, response):
        response_logging(response)
        response_attaching(response)


helper = Helper()

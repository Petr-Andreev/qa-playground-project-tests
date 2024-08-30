import logging
import json
import allure
from requests import Response
from allure_commons.types import AttachmentType


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        request_body = response.request.body.decode('utf-8') if isinstance(response.request.body,
                                                                           bytes) else response.request.body
        logging.info("INFO Request body: " + request_body)
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response: Response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=response.request.method,
        name="Method",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=str(response.request.headers),
        name="Request headers",
        attachment_type=AttachmentType.TEXT,
    )
    allure.attach(
        body=str(response.status_code),
        name="Response code",
        attachment_type=AttachmentType.TEXT,
    )

    if response.request.body:
        request_body = response.request.body.decode('utf-8') if isinstance(response.request.body,
                                                                           bytes) else response.request.body
        allure.attach(
            body=json.dumps(request_body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

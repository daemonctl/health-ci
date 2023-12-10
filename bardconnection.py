import json
import logging
import os
from http import HTTPStatus

import bardapi.core

domainName = "https://bard.google.com"
logFormat = '%(asctime)s %(levelname)s %(threadName)s %(message)s'
dateFormat = '%d/%m/%Y %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=logFormat, datefmt=dateFormat)
os.environ["_BARD_API_LANG"] = "turkish"
logger = logging.getLogger(__name__)


def get_connection(input_text=None, bardapikeys=None):
    try:
        if input_text is not None:
            response_bard = bardapi.core.Bard(bardapikeys).get_answer(input_text)
            response_json = json.loads(json.dumps(response_bard, indent=2))
            get_answer(response_json)
        else:
            logger.error("Input text not nullable")
    except Exception as err:
        print(f"Unexpected {err=}, (err)")


def get_answer(response):
    response_json = response
    if response_json['status_code'] == HTTPStatus.OK:
        content = response_json['content']
        print(content)


def main():
    pass


if __name__ == '__main__':
    main()

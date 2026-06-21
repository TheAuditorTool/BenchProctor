# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json
import os


async def BenchmarkTest64174(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    logging.info('User action: ' + str(data))
    return {"updated": True}

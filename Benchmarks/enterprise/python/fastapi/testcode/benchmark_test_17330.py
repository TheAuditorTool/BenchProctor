# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json


async def BenchmarkTest17330(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    logging.info('User action: ' + str(data))
    return {"updated": True}

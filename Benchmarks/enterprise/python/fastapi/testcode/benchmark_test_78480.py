# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest78480(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest01678(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import json
from app_runtime import auth_check


async def BenchmarkTest08614(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
from app_runtime import auth_check


async def BenchmarkTest53573(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    auth_check('user', data)
    return {"updated": True}

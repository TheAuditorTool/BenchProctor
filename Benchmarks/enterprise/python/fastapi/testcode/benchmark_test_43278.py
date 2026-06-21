# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest43278(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    auth_check('user', data)
    return {"updated": True}

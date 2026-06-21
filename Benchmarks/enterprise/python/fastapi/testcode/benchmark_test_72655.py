# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest72655(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return {"updated": True}

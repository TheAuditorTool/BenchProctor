# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest49136(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    auth_check('user', data)
    return {"updated": True}

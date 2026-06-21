# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest08005(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(cookie_value)
    data = collected
    auth_check('user', data)
    return {"updated": True}

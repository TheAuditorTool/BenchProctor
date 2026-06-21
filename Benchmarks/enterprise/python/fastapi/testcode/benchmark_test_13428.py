# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13428(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    globals().setdefault('_secret_cache', {})['current'] = str(cookie_value)
    return {"updated": True}

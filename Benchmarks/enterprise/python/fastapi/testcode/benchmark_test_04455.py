# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest04455(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}

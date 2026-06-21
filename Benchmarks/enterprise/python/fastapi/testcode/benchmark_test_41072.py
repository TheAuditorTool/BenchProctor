# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41072(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}

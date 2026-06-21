# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41953(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}

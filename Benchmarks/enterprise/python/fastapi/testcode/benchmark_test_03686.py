# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03686(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

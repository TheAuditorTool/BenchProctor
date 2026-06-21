# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest42949(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

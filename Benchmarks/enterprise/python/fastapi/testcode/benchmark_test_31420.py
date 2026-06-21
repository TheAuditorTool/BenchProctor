# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest31420(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

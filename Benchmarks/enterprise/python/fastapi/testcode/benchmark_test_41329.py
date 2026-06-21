# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest41329(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

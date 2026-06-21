# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06464(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

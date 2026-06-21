# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote


async def BenchmarkTest12837(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

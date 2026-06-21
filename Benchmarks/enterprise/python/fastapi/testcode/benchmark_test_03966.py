# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03966(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09068(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

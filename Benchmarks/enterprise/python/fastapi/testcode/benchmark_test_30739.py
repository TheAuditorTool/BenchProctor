# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30739(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

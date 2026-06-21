# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43768(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    int(str(data))
    return {"updated": True}

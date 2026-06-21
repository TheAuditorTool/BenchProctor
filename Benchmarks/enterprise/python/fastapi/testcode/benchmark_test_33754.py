# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33754(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    eval(str(data))
    return {"updated": True}

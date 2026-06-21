# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest62555(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    eval(str(data))
    return {"updated": True}

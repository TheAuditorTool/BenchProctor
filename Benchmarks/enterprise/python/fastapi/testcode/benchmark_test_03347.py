# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03347(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    eval(str(data))
    return {"updated": True}

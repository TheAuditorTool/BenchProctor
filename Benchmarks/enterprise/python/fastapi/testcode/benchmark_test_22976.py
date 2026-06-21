# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22976(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}

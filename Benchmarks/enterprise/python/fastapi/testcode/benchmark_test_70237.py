# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70237(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest79170(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}

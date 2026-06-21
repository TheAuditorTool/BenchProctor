# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest27361(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return {"updated": True}

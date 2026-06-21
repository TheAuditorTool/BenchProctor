# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest17416(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}

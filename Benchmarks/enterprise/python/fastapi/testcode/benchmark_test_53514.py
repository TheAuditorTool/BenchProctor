# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53514(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(cookie_value))
    return {"updated": True}

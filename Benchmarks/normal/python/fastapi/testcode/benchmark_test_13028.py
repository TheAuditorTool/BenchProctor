# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest13028(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}

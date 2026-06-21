# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06836(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}

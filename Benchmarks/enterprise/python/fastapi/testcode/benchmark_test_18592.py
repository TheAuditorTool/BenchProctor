# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest18592(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return {"updated": True}

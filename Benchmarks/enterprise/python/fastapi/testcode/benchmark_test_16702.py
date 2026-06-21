# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest16702(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}

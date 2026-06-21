# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest13365(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}

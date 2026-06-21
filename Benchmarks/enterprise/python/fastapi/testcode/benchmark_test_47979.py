# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest47979(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}

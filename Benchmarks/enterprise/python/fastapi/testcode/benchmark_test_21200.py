# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import base64


async def BenchmarkTest21200(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return {"updated": True}

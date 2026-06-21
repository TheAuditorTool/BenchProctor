# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import urllib.request


async def BenchmarkTest11037(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

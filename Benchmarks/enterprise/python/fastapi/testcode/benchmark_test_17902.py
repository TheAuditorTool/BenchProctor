# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest17902(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

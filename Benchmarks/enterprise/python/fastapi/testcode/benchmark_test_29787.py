# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
import urllib.parse
import ssl


def ensure_str(value):
    return str(value)

async def BenchmarkTest29787(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ensure_str(origin_value)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

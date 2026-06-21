# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest01963(request: Request):
    host_value = request.headers.get('host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

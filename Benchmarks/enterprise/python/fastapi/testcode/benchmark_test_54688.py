# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest54688(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

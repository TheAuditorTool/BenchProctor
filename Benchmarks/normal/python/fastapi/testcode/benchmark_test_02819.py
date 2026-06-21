# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import base64
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest02819(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

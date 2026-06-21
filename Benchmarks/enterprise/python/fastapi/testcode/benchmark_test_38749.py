# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest38749(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(raw_body)), context=ctx)
    return {"updated": True}

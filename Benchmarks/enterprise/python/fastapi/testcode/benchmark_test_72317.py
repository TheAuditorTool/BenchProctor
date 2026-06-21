# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest72317(request: Request):
    referer_value = request.headers.get('referer', '')
    data = default_blank(referer_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

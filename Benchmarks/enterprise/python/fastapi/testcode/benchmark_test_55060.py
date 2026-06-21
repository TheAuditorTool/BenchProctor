# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


def relay_value(value):
    return value

async def BenchmarkTest55060(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

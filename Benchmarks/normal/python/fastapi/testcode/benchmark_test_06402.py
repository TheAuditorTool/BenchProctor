# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


def normalise_input(value):
    return value.strip()

async def BenchmarkTest06402(request: Request):
    host_value = request.headers.get('host', '')
    data = normalise_input(host_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

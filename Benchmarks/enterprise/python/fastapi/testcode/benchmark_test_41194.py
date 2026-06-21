# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import urllib.request


async def BenchmarkTest41194(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

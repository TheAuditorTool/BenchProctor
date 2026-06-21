# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest01148(request: Request):
    origin_value = request.headers.get('origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

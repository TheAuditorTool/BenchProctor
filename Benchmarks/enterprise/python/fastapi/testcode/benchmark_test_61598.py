# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest61598(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = forwarded_ip if forwarded_ip else 'default'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

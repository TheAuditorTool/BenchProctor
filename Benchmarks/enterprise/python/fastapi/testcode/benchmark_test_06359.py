# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest06359(request: Request):
    host_value = request.headers.get('host', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(host_value)).read()
    return {"updated": True}

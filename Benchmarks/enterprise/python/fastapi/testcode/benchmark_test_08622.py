# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest08622(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(header_value)).read()
    return {"updated": True}

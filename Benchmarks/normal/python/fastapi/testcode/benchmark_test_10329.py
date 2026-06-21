# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest10329(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = f'{header_value}'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

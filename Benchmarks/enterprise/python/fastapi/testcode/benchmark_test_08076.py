# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request


async def BenchmarkTest08076(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value}'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

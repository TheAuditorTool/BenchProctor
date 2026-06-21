# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest02230(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

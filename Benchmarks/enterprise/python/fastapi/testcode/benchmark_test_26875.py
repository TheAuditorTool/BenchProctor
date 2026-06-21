# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest26875(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

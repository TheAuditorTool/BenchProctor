# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest06109(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(multipart_value)), context=ctx)
    return {"updated": True}

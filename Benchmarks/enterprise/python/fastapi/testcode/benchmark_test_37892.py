# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest37892(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

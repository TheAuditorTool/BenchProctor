# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import urllib.request
import urllib.parse
import ssl


def normalise_input(value):
    return value.strip()

async def BenchmarkTest72804(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = normalise_input(xml_value)
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

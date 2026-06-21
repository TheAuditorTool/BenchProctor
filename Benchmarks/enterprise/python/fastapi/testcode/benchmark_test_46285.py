# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
import urllib.request
import urllib.parse
import ssl


async def BenchmarkTest46285(request: Request, field: str = Form('')):
    field_value = field
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(field_value)), context=ctx)
    return {"updated": True}

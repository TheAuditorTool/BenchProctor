# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
import urllib.request
import urllib.parse
import ssl


request_state: dict[str, str] = {}

async def BenchmarkTest57527(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
import urllib.request
import urllib.parse
import ssl


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03931(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

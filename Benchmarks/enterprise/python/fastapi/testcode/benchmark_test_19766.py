# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import urllib.request
import urllib.parse
import ssl


@dataclass
class FormData:
    payload: str

async def BenchmarkTest19766(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    ctx = ssl.create_default_context()
    ctx.set_ciphers('aNULL')
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

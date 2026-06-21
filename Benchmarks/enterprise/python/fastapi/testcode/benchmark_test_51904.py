# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import urllib.request
import urllib.parse
import ssl


@dataclass
class FormData:
    payload: str

async def BenchmarkTest51904(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return {"updated": True}

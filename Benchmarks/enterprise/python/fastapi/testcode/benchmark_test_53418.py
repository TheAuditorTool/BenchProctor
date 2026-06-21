# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import urllib.request


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53418(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}

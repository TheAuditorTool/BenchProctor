# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest19496(request: Request):
    referer_value = request.headers.get('referer', '')
    data = FormData(payload=referer_value).payload
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import requests


@dataclass
class FormData:
    payload: str

async def BenchmarkTest38438(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}

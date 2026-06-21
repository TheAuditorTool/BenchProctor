# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import requests


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09537(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest63761(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}

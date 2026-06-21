# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest46566(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}

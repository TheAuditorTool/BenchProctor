# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest30387(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}

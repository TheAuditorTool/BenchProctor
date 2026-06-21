# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


request_state: dict[str, str] = {}

async def BenchmarkTest08526(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}

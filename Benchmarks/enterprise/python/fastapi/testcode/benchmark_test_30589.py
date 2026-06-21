# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


request_state: dict[str, str] = {}

async def BenchmarkTest30589(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}

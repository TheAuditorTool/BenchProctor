# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


request_state: dict[str, str] = {}

async def BenchmarkTest06183(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}

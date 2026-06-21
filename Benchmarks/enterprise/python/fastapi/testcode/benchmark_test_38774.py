# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


request_state: dict[str, str] = {}

async def BenchmarkTest38774(request: Request):
    upload_name = (await request.form()).get('upload', '')
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}

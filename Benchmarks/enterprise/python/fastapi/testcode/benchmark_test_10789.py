# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest10789(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}

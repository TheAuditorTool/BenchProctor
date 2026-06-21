# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest06511(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}

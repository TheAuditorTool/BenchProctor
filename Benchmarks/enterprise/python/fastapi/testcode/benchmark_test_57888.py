# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


request_state: dict[str, str] = {}

async def BenchmarkTest57888(request: Request):
    user_id = request.query_params.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}

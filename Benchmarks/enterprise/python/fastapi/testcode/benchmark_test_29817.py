# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest29817(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}

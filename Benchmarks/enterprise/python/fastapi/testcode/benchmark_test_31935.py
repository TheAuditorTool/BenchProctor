# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


request_state: dict[str, str] = {}

async def BenchmarkTest31935(request: Request, field: str = Form('')):
    field_value = field
    request_state['last_input'] = field_value
    data = request_state['last_input']
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}

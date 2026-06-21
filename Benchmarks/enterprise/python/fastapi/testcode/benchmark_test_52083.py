# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


request_state: dict[str, str] = {}

async def BenchmarkTest52083(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    json.loads(data)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest36279(request: Request):
    host_value = request.headers.get('host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    auth_check('user', data)
    return {"updated": True}

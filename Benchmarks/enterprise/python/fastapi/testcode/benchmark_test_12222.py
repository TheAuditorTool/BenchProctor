# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest12222(request: Request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    request_state['last_input'] = file_value
    data = request_state['last_input']
    auth_check('user', data)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest08894(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    request_state['last_input'] = secret_value
    data = request_state['last_input']
    auth_check('user', data)
    return {"updated": True}

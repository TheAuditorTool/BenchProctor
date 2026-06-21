# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


request_state: dict[str, str] = {}

async def BenchmarkTest08620(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    auth_check('user', data)
    return {"updated": True}

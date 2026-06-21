# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


request_state: dict[str, str] = {}

async def BenchmarkTest32131(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    request.session['data'] = str(data)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time


request_state: dict[str, str] = {}

async def BenchmarkTest79198(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import os
import time


request_state: dict[str, str] = {}

async def BenchmarkTest53488(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        return RedirectResponse(url=str(data))
    return {"updated": True}

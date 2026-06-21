# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
import re
import os
from starlette.responses import JSONResponse


request_state: dict[str, str] = {}

async def BenchmarkTest66389(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    globals()['counter'] = int(processed)
    return {"updated": True}

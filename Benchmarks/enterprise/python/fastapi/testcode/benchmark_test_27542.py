# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
import os
from starlette.responses import JSONResponse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest27542(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})

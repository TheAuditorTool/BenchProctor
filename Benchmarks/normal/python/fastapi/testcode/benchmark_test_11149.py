# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import re
from starlette.responses import JSONResponse
import subprocess


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest11149(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return {"updated": True}

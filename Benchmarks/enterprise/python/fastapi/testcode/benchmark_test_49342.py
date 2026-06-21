# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse


async def BenchmarkTest49342(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

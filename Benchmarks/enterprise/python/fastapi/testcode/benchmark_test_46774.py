# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest46774(request: Request):
    ua_value = request.headers.get('user-agent', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

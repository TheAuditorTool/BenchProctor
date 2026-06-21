# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt
import re
from starlette.responses import JSONResponse


async def BenchmarkTest45348(request: Request):
    secret_value = 'config_secret_test_abc123'
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(secret_value)
    data = collected
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return {"updated": True}

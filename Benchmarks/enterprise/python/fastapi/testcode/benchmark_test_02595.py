# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import base64
from starlette.responses import JSONResponse


async def BenchmarkTest02595(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

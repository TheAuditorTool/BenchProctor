# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest13185(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ensure_str(raw_body)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

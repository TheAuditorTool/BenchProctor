# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest65408(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = to_text(ua_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest41799(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

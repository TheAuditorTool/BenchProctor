# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest59451(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

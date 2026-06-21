# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest44470(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

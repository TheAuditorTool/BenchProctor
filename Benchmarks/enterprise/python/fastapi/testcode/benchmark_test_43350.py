# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest43350(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = normalise_input(forwarded_ip)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

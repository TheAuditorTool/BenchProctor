# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest45364(request: Request):
    origin_value = request.headers.get('origin', '')
    data = relay_value(origin_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest03930(request: Request):
    origin_value = request.headers.get('origin', '')
    data = normalise_input(origin_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def normalise_input(value):
    return value.strip()

async def BenchmarkTest70824(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

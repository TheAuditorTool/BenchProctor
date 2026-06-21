# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest55129(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

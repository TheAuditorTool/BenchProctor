# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest12274(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

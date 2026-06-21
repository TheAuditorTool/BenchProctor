# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest80626(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

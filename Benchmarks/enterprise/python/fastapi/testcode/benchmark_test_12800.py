# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest12800(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

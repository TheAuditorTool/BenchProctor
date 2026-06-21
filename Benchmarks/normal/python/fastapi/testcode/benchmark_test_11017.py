# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest11017(request: Request):
    origin_value = request.headers.get('origin', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

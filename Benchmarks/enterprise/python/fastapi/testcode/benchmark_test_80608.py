# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest80608(request: Request):
    ua_value = request.headers.get('user-agent', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

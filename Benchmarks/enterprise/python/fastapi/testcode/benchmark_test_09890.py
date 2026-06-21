# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest09890(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    pending = list(str(cookie_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

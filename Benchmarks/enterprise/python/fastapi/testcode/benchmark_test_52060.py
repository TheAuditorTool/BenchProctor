# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest52060(request: Request):
    referer_value = request.headers.get('referer', '')
    data = relay_value(referer_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

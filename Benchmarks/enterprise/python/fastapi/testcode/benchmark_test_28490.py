# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest28490(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)

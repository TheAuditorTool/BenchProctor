# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest33513(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)

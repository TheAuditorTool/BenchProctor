# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest48821(request: Request):
    ua_value = request.headers.get('user-agent', '')
    digest = str(ua_value).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)

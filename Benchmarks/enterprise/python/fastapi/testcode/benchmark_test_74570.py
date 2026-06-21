# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest74570(request: Request):
    ua_value = request.headers.get('user-agent', '')
    digest = hashlib.sha1(str(ua_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

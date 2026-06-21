# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest55506(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    digest = hashlib.sha256(str(header_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

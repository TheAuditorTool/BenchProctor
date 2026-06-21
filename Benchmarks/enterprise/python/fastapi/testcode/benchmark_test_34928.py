# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest34928(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

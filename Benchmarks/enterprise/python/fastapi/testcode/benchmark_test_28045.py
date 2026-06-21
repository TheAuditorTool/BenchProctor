# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest28045(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)

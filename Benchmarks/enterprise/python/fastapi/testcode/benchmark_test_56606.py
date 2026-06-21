# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest56606(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

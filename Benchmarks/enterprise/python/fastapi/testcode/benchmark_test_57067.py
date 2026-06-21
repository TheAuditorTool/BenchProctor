# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest57067(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)

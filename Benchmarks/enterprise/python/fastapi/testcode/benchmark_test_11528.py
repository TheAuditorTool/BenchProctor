# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest11528(request: Request):
    origin_value = request.headers.get('origin', '')
    digest = hashlib.md5(str(origin_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

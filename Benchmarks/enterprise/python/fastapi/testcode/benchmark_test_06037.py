# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest06037(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '%s' % (origin_value,)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)

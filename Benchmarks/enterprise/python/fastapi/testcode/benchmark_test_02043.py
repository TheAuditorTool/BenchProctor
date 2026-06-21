# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest02043(request: Request):
    referer_value = request.headers.get('referer', '')
    digest = hashlib.sha256(str(referer_value).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

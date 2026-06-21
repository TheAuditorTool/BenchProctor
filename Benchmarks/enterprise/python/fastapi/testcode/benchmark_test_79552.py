# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest79552(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

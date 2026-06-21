# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest02619(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    digest = str(raw_body).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)

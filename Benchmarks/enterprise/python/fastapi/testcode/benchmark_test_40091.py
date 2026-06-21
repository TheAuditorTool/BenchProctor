# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


async def BenchmarkTest40091(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)

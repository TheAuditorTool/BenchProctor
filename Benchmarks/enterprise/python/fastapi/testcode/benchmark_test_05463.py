# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest05463(request: Request):
    auth_header = request.headers.get('authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)

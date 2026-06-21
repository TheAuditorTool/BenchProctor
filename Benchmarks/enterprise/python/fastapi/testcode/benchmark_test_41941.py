# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest41941(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = auth_header
    trusted_claim = str(processed)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)

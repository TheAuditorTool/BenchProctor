# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest47525(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = f'{auth_header}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})

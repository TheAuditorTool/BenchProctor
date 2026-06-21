# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest40301(request: Request):
    auth_header = request.headers.get('authorization', '')
    if auth_header not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = auth_header
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest75557(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    if forwarded_ip not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = forwarded_ip
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})

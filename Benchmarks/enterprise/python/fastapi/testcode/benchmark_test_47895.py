# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest47895(request: Request):
    host_value = request.headers.get('host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

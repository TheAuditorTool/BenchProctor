# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest30401(request: Request):
    host_value = request.headers.get('host', '')
    data = str(host_value).replace('\x00', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

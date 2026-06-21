# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest68145(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})

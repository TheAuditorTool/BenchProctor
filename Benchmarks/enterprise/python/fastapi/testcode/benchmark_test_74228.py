# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest74228(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest74952(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}

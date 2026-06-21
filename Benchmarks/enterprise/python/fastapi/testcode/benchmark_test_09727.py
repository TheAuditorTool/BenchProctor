# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest09727(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = auth_header if auth_header else 'default'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(data)})

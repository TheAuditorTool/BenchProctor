# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest54500(request: Request):
    host_value = request.headers.get('host', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(host_value)})

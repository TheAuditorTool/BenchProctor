# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest13987(request: Request):
    ua_value = request.headers.get('user-agent', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(ua_value)})

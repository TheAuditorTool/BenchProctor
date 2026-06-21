# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest03741(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest45077(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})

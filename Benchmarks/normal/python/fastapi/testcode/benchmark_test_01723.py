# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest01723(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})

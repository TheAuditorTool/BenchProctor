# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest38398(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest23237(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

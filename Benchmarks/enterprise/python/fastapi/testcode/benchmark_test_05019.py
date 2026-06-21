# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest05019(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest56345(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest28129(request: Request):
    auth_header = request.headers.get('authorization', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest16219(request: Request):
    referer_value = request.headers.get('referer', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

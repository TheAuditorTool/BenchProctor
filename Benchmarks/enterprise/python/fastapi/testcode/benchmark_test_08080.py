# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest08080(request: Request):
    referer_value = request.headers.get('referer', '')
    data = relay_value(referer_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

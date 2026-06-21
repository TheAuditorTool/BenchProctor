# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest72003(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ensure_str(ua_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

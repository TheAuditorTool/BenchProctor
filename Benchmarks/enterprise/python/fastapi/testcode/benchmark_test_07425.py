# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def ensure_str(value):
    return str(value)

async def BenchmarkTest07425(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

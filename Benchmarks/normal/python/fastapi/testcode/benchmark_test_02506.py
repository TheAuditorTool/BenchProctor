# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest02506(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = relay_value(header_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

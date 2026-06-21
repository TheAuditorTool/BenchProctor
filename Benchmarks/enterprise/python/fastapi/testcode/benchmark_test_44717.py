# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest44717(request: Request):
    origin_value = request.headers.get('origin', '')
    data = default_blank(origin_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

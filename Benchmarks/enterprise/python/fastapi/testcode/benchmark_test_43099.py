# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest43099(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = coalesce_blank(header_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

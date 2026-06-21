# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest06655(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

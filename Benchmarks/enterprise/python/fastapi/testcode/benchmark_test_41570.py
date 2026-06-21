# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest41570(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

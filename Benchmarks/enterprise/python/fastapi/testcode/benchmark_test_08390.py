# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest08390(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value:.200s}'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

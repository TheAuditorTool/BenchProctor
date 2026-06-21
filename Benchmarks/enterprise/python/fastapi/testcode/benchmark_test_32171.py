# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest32171(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

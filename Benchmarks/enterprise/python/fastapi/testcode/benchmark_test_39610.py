# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest39610(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest33769(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest06712(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = relay_value(forwarded_ip)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

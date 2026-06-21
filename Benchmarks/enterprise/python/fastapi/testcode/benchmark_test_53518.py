# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest53518(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

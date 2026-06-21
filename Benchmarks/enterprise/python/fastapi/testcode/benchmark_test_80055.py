# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest80055(request: Request):
    host_value = request.headers.get('host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

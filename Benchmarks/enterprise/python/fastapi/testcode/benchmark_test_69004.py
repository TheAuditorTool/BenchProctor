# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest69004(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = relay_value(ua_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)

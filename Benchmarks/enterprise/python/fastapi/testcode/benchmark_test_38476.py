# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest38476(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = relay_value(auth_header)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)

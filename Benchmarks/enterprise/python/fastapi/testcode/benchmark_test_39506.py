# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest39506(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)

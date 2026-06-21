# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest77248(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}

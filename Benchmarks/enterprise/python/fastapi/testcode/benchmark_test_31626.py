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

async def BenchmarkTest31626(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}

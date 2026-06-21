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

async def BenchmarkTest16581(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    trusted_claim = str(data)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)

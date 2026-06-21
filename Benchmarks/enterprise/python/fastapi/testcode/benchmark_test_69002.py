# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest69002(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

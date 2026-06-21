# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from fastapi import Form
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest01059(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)

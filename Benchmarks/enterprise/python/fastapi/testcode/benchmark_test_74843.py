# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import random
from fastapi import Form
from starlette.responses import JSONResponse


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest74843(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return JSONResponse({'token': str(token)}, status_code=200)

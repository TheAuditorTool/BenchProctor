# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest13328(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)

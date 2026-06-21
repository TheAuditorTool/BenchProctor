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

async def BenchmarkTest73761(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}

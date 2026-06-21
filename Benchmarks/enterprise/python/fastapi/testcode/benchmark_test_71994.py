# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest71994(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    if time.time() > 1000000000:
        return RedirectResponse(url=str(data))
    return {"updated": True}

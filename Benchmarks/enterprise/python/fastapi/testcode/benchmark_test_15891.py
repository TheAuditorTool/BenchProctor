# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest15891(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

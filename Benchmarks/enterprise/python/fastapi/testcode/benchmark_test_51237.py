# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest51237(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}

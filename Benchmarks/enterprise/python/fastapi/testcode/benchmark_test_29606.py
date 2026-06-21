# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest29606(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = handle(upload_name)
    result = 100 / int(str(data))
    return {"updated": True}

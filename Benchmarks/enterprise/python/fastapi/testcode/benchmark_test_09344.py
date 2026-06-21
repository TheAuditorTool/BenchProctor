# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest09344(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    auth_check('user', data)
    return {"updated": True}

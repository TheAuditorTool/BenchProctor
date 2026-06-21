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

async def BenchmarkTest43538(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    processed = data[:64]
    auth_check('user', processed)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest58797(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}

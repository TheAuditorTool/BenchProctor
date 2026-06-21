# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest65330(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    yaml.safe_load(data)
    return {"updated": True}

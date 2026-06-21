# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest00541(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    os.seteuid(65534)
    return {"updated": True}

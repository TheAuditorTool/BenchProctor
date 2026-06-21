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

async def BenchmarkTest70055(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}

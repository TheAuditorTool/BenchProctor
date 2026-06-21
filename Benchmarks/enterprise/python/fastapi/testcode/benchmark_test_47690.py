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

async def BenchmarkTest47690(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    os.remove(str(data))
    return {"updated": True}

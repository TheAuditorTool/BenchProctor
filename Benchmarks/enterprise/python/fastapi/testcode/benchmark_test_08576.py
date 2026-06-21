# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest08576(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    if time.time() > 1000000000:
        yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}

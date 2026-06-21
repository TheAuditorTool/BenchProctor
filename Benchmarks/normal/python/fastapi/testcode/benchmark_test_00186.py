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

async def BenchmarkTest00186(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return {"updated": True}

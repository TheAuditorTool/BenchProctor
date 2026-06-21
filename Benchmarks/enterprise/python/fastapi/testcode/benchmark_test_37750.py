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

async def BenchmarkTest37750(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = handle(xml_value)
    auth_check('user', data)
    return {"updated": True}

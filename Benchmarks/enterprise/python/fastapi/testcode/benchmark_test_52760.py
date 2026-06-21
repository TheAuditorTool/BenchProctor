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

async def BenchmarkTest52760(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = handle(config_value)
    auth_check('user', data)
    return {"updated": True}

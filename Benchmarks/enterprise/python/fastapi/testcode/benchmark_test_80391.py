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

async def BenchmarkTest80391(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = handle(secret_value)
    auth_check('user', data)
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest41911(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    auth_check('user', data)
    return {"updated": True}

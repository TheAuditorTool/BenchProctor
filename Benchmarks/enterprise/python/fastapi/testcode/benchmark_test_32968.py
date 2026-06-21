# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest32968(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}

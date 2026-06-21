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

async def BenchmarkTest12033(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    os.remove(str(data))
    return {"updated": True}

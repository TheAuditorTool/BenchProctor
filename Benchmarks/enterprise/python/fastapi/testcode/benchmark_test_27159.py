# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest27159(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}

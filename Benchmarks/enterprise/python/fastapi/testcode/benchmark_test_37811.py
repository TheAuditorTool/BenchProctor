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

async def BenchmarkTest37811(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    await _evasion_task()
    return {"updated": True}

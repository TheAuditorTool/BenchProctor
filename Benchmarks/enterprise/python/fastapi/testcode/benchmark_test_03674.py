# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import pickle


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest03674(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = handle(ua_value)
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    await _evasion_task()
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest29769(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    async def _evasion_task():
        requests.get(str(data))
    await _evasion_task()
    return {"updated": True}

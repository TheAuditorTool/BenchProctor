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

async def BenchmarkTest74994(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}

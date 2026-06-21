# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest69277(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}

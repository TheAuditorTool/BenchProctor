# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest43054(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = handle(forwarded_ip)
    def _primary():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}

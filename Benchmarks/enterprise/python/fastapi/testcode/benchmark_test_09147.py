# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest09147(request: Request, field: str = Form('')):
    field_value = field
    data = handle(field_value)
    def _primary():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}

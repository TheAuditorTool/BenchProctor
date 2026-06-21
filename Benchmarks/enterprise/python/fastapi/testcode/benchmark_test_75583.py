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

async def BenchmarkTest75583(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}

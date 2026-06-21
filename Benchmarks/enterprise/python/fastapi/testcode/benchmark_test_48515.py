# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest48515(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}

# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest61682(request: Request):
    referer_value = request.headers.get('referer', '')
    data = handle(referer_value)
    processed = data[:64]
    db.users.find({'$where': "this.username == '" + str(processed) + "'"})
    return {"updated": True}

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

async def BenchmarkTest53447(request: Request):
    user_id = request.query_params.get('id', '')
    data = handle(user_id)
    if time.time() > 1000000000:
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    return {"updated": True}

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

async def BenchmarkTest68893(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = handle(comment_value)
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    return {"updated": True}

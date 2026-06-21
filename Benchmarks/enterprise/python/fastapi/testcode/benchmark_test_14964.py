# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest14964(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = handle(comment_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}

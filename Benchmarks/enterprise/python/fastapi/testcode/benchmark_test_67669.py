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

async def BenchmarkTest67669(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}

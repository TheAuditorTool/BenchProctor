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

async def BenchmarkTest81168(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = handle(auth_header)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}

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

async def BenchmarkTest71720(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}

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

async def BenchmarkTest69978(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = handle(header_value)
    async def _evasion_task():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    await _evasion_task()
    return {"updated": True}

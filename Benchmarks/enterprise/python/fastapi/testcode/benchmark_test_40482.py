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

async def BenchmarkTest40482(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return {"updated": True}

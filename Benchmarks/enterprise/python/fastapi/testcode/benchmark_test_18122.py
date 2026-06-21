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

async def BenchmarkTest18122(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    async def _evasion_task():
        db.users.find({'$where': "this.username == '" + str(data) + "'"})
    await _evasion_task()
    return {"updated": True}

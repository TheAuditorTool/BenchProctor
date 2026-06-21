# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
from app_runtime import db


async def BenchmarkTest70130(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return {"updated": True}

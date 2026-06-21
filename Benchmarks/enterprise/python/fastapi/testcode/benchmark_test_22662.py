# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest22662(request: Request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = handle(dotenv_value)
    auth_check('user', data)
    return {"updated": True}

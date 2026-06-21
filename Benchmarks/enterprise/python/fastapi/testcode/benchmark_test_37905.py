# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest37905(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    auth_check('user', data)
    return {"updated": True}

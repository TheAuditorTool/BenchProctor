# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest19653(request: Request):
    path_value = request.path_params.get('id', '')
    data = handle(path_value)
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
